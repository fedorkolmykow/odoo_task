# -*- coding: utf-8 -*-
from odoo import http
import os

PATH_TO_SHARE = '/tmp'

class OdooShareFedorkolmykow(http.Controller):
    @http.route('/odoo_share_fedorkolmykow/odoo_share_fedorkolmykow/', auth='user', methods=['GET', 'POST'], website=True)
    def upload(self, **kw):
        user = http.request.env['res.users'].browse(http.request.session.pre_uid)

        if not user.has_group('base.group_erp_manager'):
            return

        path = os.getenv('PATH_TO_SHARE', PATH_TO_SHARE)
        if kw.get('File', False):
            name = kw.get('File').filename
            file = kw.get('File')
            file.save(os.path.join(path, name))
        files = os.listdir(path)
        return http.request.render('odoo_share_fedorkolmykow.uploading', {
            'files': files,
        })

    @http.route('/odoo_share_fedorkolmykow/odoo_share_fedorkolmykow/download/<file>', auth='public')
    def download(self, file, **kw):
        path = os.getenv('PATH_TO_SHARE', PATH_TO_SHARE)
        return http.send_file(os.path.join(path, file))
