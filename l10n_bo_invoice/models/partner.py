from openerp import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    document_number = fields.Char('Numero de Documento de Identidad', size=32)
    document_issued = fields.Char('Lugar de emision del Documento Identidad', size=32)

    @api.onchange('document_number', 'document_type_id')
    def onchange_document(self):
        pass
