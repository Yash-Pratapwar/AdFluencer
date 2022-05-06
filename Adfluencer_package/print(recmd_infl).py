# print(recmd_infl)
        # a = recmd_infl[0]
        # print(a)
        # recm_infl_lst = []
        # recm_infl_lst = recm_infl_lst.extend(a)
        # lst_2 = recmd_infl[2:]
        # recm_infl_lst.extend(lst_2)
        # print(recm_infl_lst)
        # print(advts)
        # main=[]
        # for inf_id in recm_infl_lst:
        #     inf = users.query.filter_by(id=inf_id)
        #     for infl in inf:
        #         f = infl.fname
        #         l = infl.lname
        #         c = infl.categories
        #         s = infl.smh
        #         abc=[]
        #         abc.append(f)
        #         abc.append(l)
        #         abc.append(c)
        #         abc.append(s)
        #         main.append(abc)
            # print(inf)
        #     for infl in inf:
        #         advt_id = current_user.id
        #         inf_id = infl.id
        #         inf_fname = infl.fname
        #         inf_lname = infl.lname
        #         inf_email = infl.inf_email
        #         inf_smh = infl.smh
        #         categories = infl.categories
        #         # print(advt_id, inf_id, inf_fname)
        #         # filename = secure_filename(prdt_imgs.filename)
        #         # mimetype = prdt_imgs.mimetype
        #         # file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))
        #         recm_inf = recm_infl(advt_id=advt_id, inf_id=inf_id,inf_fname=inf_fname, 
        #         inf_lname=inf_lname, inf_email=inf_email, inf_smh=inf_smh, categories=categories)
        #         db.session.add(recm_inf)
        #         db.session.commit()
        # reccommended_infl = recm_infl.query.filter_by(advt_id=owner_id).limit(10).all()
        # for infl in reccommended_infl:
        #     abc_n = infl.inf_fname
        #     abc.append(abc_n)
        #     print(abc)
        # lst = []
        # for inf in abc:
        #     for infl in inf:
        #         a = infl.fname