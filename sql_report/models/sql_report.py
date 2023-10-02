# -*- coding: utf-8 -*-

import csv
import base64

from odoo import api, fields, models
from odoo.exceptions import UserError

BLACKLIST = ['insert', 'update', 'delete']


class SqlReport(models.Model):
    _name = 'sql.report'
    _description = 'Reporte SQL'
    _inherit = ['mail.activity.mixin', 'mail.thread']

    name = fields.Char(
        'Number', required=True, default='Nuevo', readonly=True)
    description = fields.Char('Description', required=True)
    select_sql = fields.Text('SQL statement', required=True, tracking=True)

    def check_select_sql(self):
        """."""
        for s in self.select_sql.split(' '):
            if s.lower() in BLACKLIST:
                raise UserError(
                    'The {} parameter is not supported.'.format(s.upper()))

    def header_csv(self, dicc):
        """."""
        return [key for key in dicc]

    def generate_report(self):
        """."""
        self.check_select_sql()
        try:
            self.env.cr.execute(self.select_sql)
        except Exception as e:
            raise UserError(str(e))

        if self.env.cr.rowcount:
            res = self.env.cr.dictfetchall()
            header = sorted(self.header_csv(res[0]))
            print(res)

            path = '/tmp/report_sql.csv'
            with open(path, mode='w',encoding='UTF-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=header)
                writer.writeheader()
                for data in res:
                    for key, val in data.items():
                        if isinstance(val, str):
                            data[key] = val.strip()
                    writer.writerow(data)

            csv_file.close()
            arch = open(path, 'r').read()
            data = base64.b64encode(bytes(arch, 'utf-8'))
            attach_vals = {
                'name': 'report-sql.csv',
                'datas': data,
                'type': 'binary',
            }
            doc_id = self.env['ir.attachment'].create(attach_vals)

            return {
                'type': "ir.actions.act_url",
                'url': "web/content/?model=ir.attachment&id={}&filename_field"
                "=datas_fname&field=datas&download=true&filename={}".format(
                    doc_id.id, doc_id.name),
                'target': '_blank',
            }
        raise UserError('Not results')

    @api.model
    def create(self, vals):
        """."""
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'sql.report') or 'Nuevo'
        return super(SqlReport, self).create(vals)
