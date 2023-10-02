# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2018 Marlon Falcón Hernandez
#    (<http://www.ynext.cl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sql Report - MFH',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'author': 'Ynext SpA',
    'maintainer': 'Ynext SpA',
    'website': 'http://www.ynext.cl',
    'summary': 'Reporte de consultas SQL.',
    'license': 'AGPL-3',
    'depends': ['base','mail'],
    'data': [
        'views/ir_sequence.xml',
        'security/group_security.xml',
        'security/ir.model.access.csv',
        'data/data_view.xml',
        'views/sql_report_view.xml'],
    'installable': True,
    'application': False,
    'auto_install': False
}
