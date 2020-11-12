# -*- coding: utf-8 -*-
from odoo import http
import os

PATH_TO_SHARE = '/home/fedor/share'

class OdooShareFedorkolmykow(http.Controller):
    @http.route('/odoo_share_fedorkolmykow/odoo_share_fedorkolmykow/', auth='user', methods=['GET', 'POST'], website=True)
    def upload(self, **kw):
        path = os.getenv('PATH_TO_SHARE', PATH_TO_SHARE)
        if kw.get('attachment', False):
            name = kw.get('attachment').filename
            file = kw.get('attachment')
            file.save(os.path.join(path, name))
        files = os.listdir(path)
        return http.request.render('odoo_share_fedorkolmykow.uploading', {
            'files': files,
        })

    @http.route('/odoo_share_fedorkolmykow/odoo_share_fedorkolmykow/download/<file>', auth='public')
    def download(self, file, **kw):
        path = os.getenv('PATH_TO_SHARE', PATH_TO_SHARE)
        return http.send_file(os.path.join(path, file))

#     @http.route('/odoo_share_fedorkolmykow/odoo_share_fedorkolmykow/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_share_fedorkolmykow.listing', {
#             'root': '/odoo_share_fedorkolmykow/odoo_share_fedorkolmykow',
#             'objects': http.request.env['odoo_share_fedorkolmykow.odoo_share_fedorkolmykow'].search([]),
#         })

#     @http.route('/odoo_share_fedorkolmykow/odoo_share_fedorkolmykow/objects/<model("odoo_share_fedorkolmykow.odoo_share_fedorkolmykow"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_share_fedorkolmykow.object', {
#             'object': obj
#         })
