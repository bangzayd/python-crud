from flask_table import Table, Col, LinkCol
 
class Results(Table):
    a0 = Col('Id', show=False)
    a1 = Col('Name')
    a9 = Col('Email')
    a2 = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='a0'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='a0'))
