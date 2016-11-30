from openerp import models, fields, api


class InvoiceDosage(models.Model):
    _name = 'l10n_bo.invoice.dosage'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    active = fields.Boolean(default=True)
    company = fields.many2one('res.company', 'Company', required=True),
    branch_office = fields.many2one('res.partner', required=False),

    nit = fields.Char()
    authorization_code = fields.Char()
    authorization_secret = fields.Char()

    valid_until_date = fields.DateField()
    valid_until_total = fields.IntegerField()


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    number = fields.Integer(compute='_get_invoice_number')
    place_printed = fields.Integer()

    cashier_name = fields.Char()
    cashier_venue = fields.Char()
    cashier = fields.One2Many()

    @api.one
    def _get_invoice_number(self):
        pass
