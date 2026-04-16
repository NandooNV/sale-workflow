# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale order revisions",
    "summary": "Keep track of revised quotations",
    "version": "19.0.1.0.0",
    "category": "Sale Management",
    "author": "Agile Business Group,"
    "Dreambits,"
    "Camptocamp,"
    "Akretion,"
    "Serpent Consulting Services Pvt. Ltd.,"
    "Ecosoft,"
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/sale-workflow",
    "license": "AGPL-3",
    "depends": ["base_revision", "sale_management"],
    "data": ["views/sale_order_views.xml"],
    "installable": True,
    "post_init_hook": "populate_unrevisioned_name",
}
