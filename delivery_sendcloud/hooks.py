# Copyright 2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, SUPERUSER_ID


def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    carriers = env["delivery.carrier"].search([("delivery_type", "=", "sendcloud")])
    carriers.write({"delivery_type": "fixed", "active": False})
