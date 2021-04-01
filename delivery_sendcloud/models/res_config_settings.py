# Copyright 2015 Salton Massally <smassally@idtlabs.sl>
# Copyright 2016 OpenSynergy Indonesia
# Copyright 2018 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    is_sendcloud_test_mode = fields.Boolean(
        related="company_id.is_sendcloud_test_mode",
        readonly=False,
    )
