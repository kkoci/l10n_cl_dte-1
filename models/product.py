from openerp import fields, models, api, _


class product_template(models.Model):
    '''
    Seleccion tipo de servicio para facturacion exportacion
    '''
    _inherit = 'product.template'

    tipo_servicio = fields.Selection([('1', 'Facturacion de Servicios Periodicos Domiciliarios'), ('2', 'Facturacion de Otros Servicios de Otros Servicios Periodicos'), ('3', 'Factura de Servicio')], required=False)
