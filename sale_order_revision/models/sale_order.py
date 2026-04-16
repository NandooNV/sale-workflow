# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models
from odoo.fields import Domain


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "base.revision"]

    current_revision_id = fields.Many2one(
        comodel_name="sale.order",
    )
    old_revision_ids = fields.One2many(
        comodel_name="sale.order",
        inverse_name="current_revision_id",
    )

    # The parent base.revision constraint covers (unrevisioned_name, revision_number)
    # only. sale.order is multi-company, so uniqueness must also include company_id.
    _revision_unique = models.UniqueIndex(
        "(unrevisioned_name, revision_number, company_id)",
        message="Order Reference and revision must be unique per Company.",
    )

    def _prepare_revision_data(self, new_revision):
        vals = super()._prepare_revision_data(new_revision)
        vals.update({"state": "cancel"})
        return vals

    def action_view_revisions(self):
        self.ensure_one()
        result = self.env["ir.actions.act_window"]._for_xml_id("sale.action_orders")
        result["domain"] = Domain(["|", ("active", "=", False), ("active", "=", True)])
        result["context"] = {
            "active_test": 0,
            "search_default_current_revision_id": self.id,
            "default_current_revision_id": self.id,
        }
        return result

    def action_back_to_current(self):
        """Navigate from an old (archived) revision to the current active revision."""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": self._name,
            "res_id": self.current_revision_id.id,
            "view_mode": "form",
            "target": "current",
        }
