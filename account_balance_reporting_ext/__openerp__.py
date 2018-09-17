# -*- coding: utf-8 -*-
# © 2017 Jacon Informatica - Javier Marhuenda <info@jacon.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0).

{
    "name": "Extensión para Account balance reporting engine",
    "version": "8.0.0.1.0",
    "author": "Jacon Informatica",
    "contributors": [
        "Javier Marhuenda <javiermarhuenda@gmail.com>",
    ],
    "license": "AGPL-3",
    "website": "http://www.jacon.es",
    "category": "Localisation/Accounting",
    "description": """
Extensión para Account balance reporting engine.
================================================

Añade titulo y descripción a los informes. Estos se podrán incorporar a los informes y dejar el nombre solo como denominación y así evitar el problema de la longitud del nombre cuando se exportan.
    """,
    "depends": [
        'account_balance_reporting',
    ],
    "demo": [],
    "data": [
        "views/account_balance_reporting_report_view_ext.xml",
    ],
    "installable": True,
}
