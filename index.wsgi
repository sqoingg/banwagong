# coding: UTF-8
import os
import sae
import web

from weixinInterface import WeixinInterface

urls = (
'/weixin','WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)

作者：段小草
链接：https://zhuanlan.zhihu.com/p/21354943
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。