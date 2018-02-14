# -*- coding: utf-8 -*-
# Copyright 2018, Jarsa Sistemas
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Openacademy',
    'summary': 'Summary of the module',
    'version': '10.0.1.0.0',
    'category': 'Academy',
    'website': 'https://www.jarsa.com.mx/',
    'author': 'Jarsa Sistemas',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'base',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/openacademy_course.xml',
        'views/openacademy_session.xml',
        'views/res_partner.xml',
    ],
    'demo': [
        'demo/openacademy_course.xml',
    ],
}
