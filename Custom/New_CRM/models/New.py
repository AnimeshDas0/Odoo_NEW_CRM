from odoo import models, fields, api
from odoo.exceptions import ValidationError


class NewModel(models.Model):
    _name = 'new'
    _description = 'New Model'

    organization_or_contact = fields.Char('Organization or Contact', required=True)
    opportunity = fields.Char('Opportunity', required=True)
    email = fields.Char('Email', required=True)
    phone = fields.Char('Phone', required=True)
    expected_revenue = fields.Float('Expected Revenue', required=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('very_high', 'Very High'),
    ], string='Priority', default='low', required=True)

    stage = fields.Selection([
        ('new', 'New'),
        ('qualified', 'Qualified'),
        ('proposition', 'Proposition'),
        ('won', 'Won'),
    ], string='Stage', default='new', required=True, track_visibility='onchange')

    @api.constrains('email')
    def _check_unique_email(self):
        for record in self:
            if self.search([('email', '=', record.email), ('id', '!=', record.id)]):
                raise ValidationError('Email must be unique!')

    @api.constrains('phone')
    def _check_phone_length(self):
        for record in self:
            if len(record.phone) > 10:
                raise ValidationError('Phone number cannot be more than 10 digits.')
            if not record.phone.isdigit():
                raise ValidationError('Phone number must contain only digits.')

    @api.model
    def action_set_priority_medium(self):
        for record in self:
            record.priority = 'medium'

    @api.model
    def action_set_priority_high(self):
        for record in self:
            record.priority = 'high'

    @api.model
    def action_set_priority_very_high(self):
        for record in self:
            record.priority = 'very_high'
