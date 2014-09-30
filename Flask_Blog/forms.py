from flask.ext.wtf import Form
from wtforms import TextField,PasswordField,TextAreaField
from wtforms.validators import Required


class foorms(Form):
    #openid=TextField('openid',validators=[Required()])
    name=TextField('name',validators=[Required()])
    sear=TextField('sear',validators=[Required()])

    head=TextField('head',validators=[Required()])
    body=TextAreaField('body')
    com=TextAreaField('com')
    #des=fields.TextAreaField('des')
    l=TextField('l',validators=[Required()])
    p=PasswordField('p',validators=[Required()])
    logi=TextField('logi',validators=[Required()])
    pasw=PasswordField('pasw',validators=[Required()])
    rly=TextAreaField('rly')
    sea=TextField('sea',validators=[Required()])
