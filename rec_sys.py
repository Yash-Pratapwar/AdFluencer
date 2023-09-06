import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pandas as pd

def recm_sys(tar_infl):
    db_engine = create_engine('postgresql://zxarian:1234@localhost:5432/adfluencer')
    sql = "COPY users TO STDOUT WITH CSV HEADER DELIMITER ','"
    with open("/home/yash/selenium_chrome/faker_updated_6.csv", "w") as file:
        conn = db_engine.raw_connection()
        cur = conn.cursor()
        cur.copy_expert(sql, file)
    infl_tags = pd.read_csv('/home/yash/selenium_chrome/faker_updated_6.csv')
    print(infl_tags)
    infl_tags.fillna("", inplace=True)    
    infl_tags_stack = infl_tags[infl_tags['categories'] != '(no categories listed)'].set_index('id').categories.str.split(',', expand = True).stack()
    infl_tags_explode = pd.get_dummies(infl_tags_stack, prefix = 'g').groupby(level = 0).sum().reset_index()
    del infl_tags_stack

    infl_tags_explode['tag_vector'] = infl_tags_explode.iloc[:,1:].values.tolist()
    infl_tags = infl_tags.merge(infl_tags_explode[['id','tag_vector']], on = 'id', how = 'left')
    infl_tags_list = infl_tags.groupby(['id','comp_name'])['categories'].apply(lambda x: ','.join(x)).reset_index()
    infl_tags_list['tag_list'] = infl_tags_list.categories.map(lambda x: x.split(','))

    infl_tags_list.loc[infl_tags_list.comp_name == tar_infl, ['id','comp_name','tag_list']]

    target_infl = tar_infl

    target_tag_list = infl_tags_list[infl_tags_list.comp_name == target_infl].tag_list.values[0]
    infl_tags_list_sim = infl_tags_list[['id','comp_name','tag_list','categories']].copy()
    infl_tags_list_sim['jaccard_sim'] = infl_tags_list_sim.tag_list.map(lambda x: len(set(x).intersection(set(target_tag_list))) / len(set(x).union(set(target_tag_list))))

    text = ','.join(infl_tags_list_sim.sort_values(by = 'jaccard_sim', ascending = False).head(25)['categories'].values)

    a = infl_tags_list_sim.sort_values(by = 'jaccard_sim', ascending = False).id.head(15)
    print([a])

    b = []
    for item in a:
        b.append(item)
    
    return b

# op = recm_sys('Faasos')
# print(op)