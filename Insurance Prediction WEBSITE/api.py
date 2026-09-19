from flask import *
from database import *
from newcnn import predictcnn

import json



api=Blueprint('api',__name__)

@api.route('/reg',methods=['get','post'])
def reg():
	data={}
	fname=request.args['fname']
	lname=request.args['lname']
	gender=request.args['gender']
	place=request.args['place']
	pin=request.args['pincode']
	phone=request.args['phone']
	email=request.args['email'] 
	uname=request.args['username'] 
	passw=request.args['password'] 

	q="select * from login where username='%s'"%(uname)
	res=select(q)
	if res:
	   data['status']="duplicate"
	else:
	    q="insert into `login` values(NULL,'%s','%s','agent')"%(uname,passw)
	    res=insert(q)

	    w="insert into agent value(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fname,lname,gender,place,pin,email,phone)
	    insert(w)

	data['status']="success"
	return str(data)


@api.route('/logins',methods=['post','get'])
def logins():
	data={}
	uname=request.args['username']
	pasw =request.args['password']
	q="select * from login where username='%s' and password='%s'"%(uname,pasw)
	res=select(q)
	data['data']=res
	data['status']="success"
	return str(data)


@api.route('/agent_view_policy')
def agent_view_policy():
	data={}
	q="select * from policy"
	res=select(q)
	data['data']=res
	data['status']="success"
	return str(data)



@api.route('/agent_request_policy',methods=['get','post'])
def agent_request_policy():
    data={}
    pid=request.args['pid']
   
    vnum=request.args['vnum']
    mnum=request.args['mnum']
    enum=request.args['enum']
    aid=request.args['login_id']

    q="insert into policyrequest values (null,(select agent_id from agent where login_id='%s'),'%s','%s','%s','%s',curdate(),'pending')"%(aid,pid,vnum,mnum,enum)
    insert(q)
    data['status']="success"
    data['method']="user_requestacc"
    return str(data)



@api.route('/agent_view_mypolicyreq')
def agent_view_mypolicyreq():
    data={}
    lid=request.args['login_id']
    q="select * from policy inner join policyrequest using (policy_id) where agent_id=(select agent_id from agent where login_id='%s')"%(lid)
    print(q)
    res=select(q)
    if res:
        data['status']='success'

    
   
        data['data']=res
    else:

        data['status']="failed"
    return str(data)


@api.route('/dropdownpolicy')
def dropdownpolicy():
    data={}
    lid=request.args['id']
    q="select * from policyrequest where agent_id=(select agent_id from agent where login_id='%s') and status='Approved'"%(lid)
    res=select(q)

    data['data']=res
    data['status']="success"
    data['method']="viewproductspinner"
    return str(data)




import uuid
@api.route('/agent_damage_request/',methods=['get','post'])
def agent_damage_request():
    data={}
    amount=""
   
    log_id=request.form['log_id']
   
    plid=request.form['pid']
    image1=request.files['image']
    path1="static/uploads/"+str(uuid.uuid4())+image1.filename
    image1.save(path1)
    image2=request.files['image1']
    path2="static/uploads/"+str(uuid.uuid4())+image2.filename
    image2.save(path2)
    image3=request.files['image2']
    path3="static/uploads/"+str(uuid.uuid4())+image3.filename
    image3.save(path3)
    image4=request.files['image3']
    path4="static/uploads/"+str(uuid.uuid4())+image4.filename
    image4.save(path4)


    q="select * from policy inner join policyrequest using (policy_id)"
    res=select(q)




    res=predictcnn(path1)


    msg=""
    amount=""
    if str(res)=="0":
        msg="10"
        amount="15000"
    elif str(res)=="1":
        msg="30"
        amount="28000"

    elif str(res)=="2":
    	msg="50"
    	amount="50000"

    elif str(res)=="3":
        msg="unverified"
        amount="Unverified"
    print ("sssssssssssssssssssssssssssssssssss",msg)
    q="insert into damagerequest values (null,(select agent_id from agent where login_id='%s'),'%s','%s','%s',curdate(),'pending','%s','%s','%s')"%(log_id,plid,path1,msg,path2,path3,path4)
    id=insert(q)
    data['status']="success"
    data['method']="upload_image"
    return str(data)
       
   

@api.route('/agent_view_damagereq')
def agent_view_damagereq():
    data={}
    lid=request.args['login_id']
    q="select *,damagerequest.date as date,damagerequest.status as status  from policy inner join policyrequest using (policy_id) inner join damagerequest using (policyrequest_id)  where damagerequest.agent_id=(select agent_id from agent where login_id='%s')"%(lid)
    res=select(q)
    print(q)
    data['data']=res
    data['status']="success"
    return str(data)


@api.route('/agent_view_damagereqs')
def agent_view_damagereqs():
    data={}
    lid=request.args['login_id']
    did=request.args['did']
    q="select *,damagerequest.date as date,damagerequest.status as status  from policy inner join policyrequest using (policy_id) inner join damagerequest using (policyrequest_id)  where damagerequest.agent_id=(select agent_id from agent where login_id='%s')  and damagerequest_id='%s'"%(lid,did)
    res=select(q)
    print(q)
    data['data']=res
    data['status']="success"
    return str(data)



   





@api.route("/agent_send_complaint",methods=['get','post'])
def agent_send_complaint():
    data={}

    cid=request.args['login_id']
    comp=request.args['complaint']

    q="insert into complaint values(NULL,(select agent_id from agent where login_id='%s'),'%s','pending',curdate())"%(cid,comp)
    insert(q)
    data['status']="success"
    data['method']="send_complaint"
    return str(data)



@api.route('/view_complaints')
def view_complaints():
    data={}
    cid=request.args['login_id']
    q="select * from complaint where agent_id=(select agent_id from agent where login_id='%s')"%(cid)
    print(q)
    res=select(q)
    data['status']='success'
    data['data']=res
    data['method']="view_complaints"
    return str(data)


        
      
    



           