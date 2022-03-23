from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class InheritPlanningSlot(models.Model):
    _inherit = 'planning.slot'

    @api.model
    def action_copy_previous_month(self, date_end_month):

        date_end_month_copy = datetime.strptime(date_end_month, DEFAULT_SERVER_DATETIME_FORMAT)
        date_start_month_copy = date_end_month_copy.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        domain = [
            ('start_datetime', '>=', date_start_month_copy),
            ('end_datetime', '<=', date_end_month_copy),
            ('recurrency_id', '=', False),
            ('was_copied', '=', False)
        ]

        slots_to_copy = self.search(domain)

        new_slot_values = []
        for slot in slots_to_copy:
            if not slot.was_copied:
                values = slot.copy_data()[0]
                if values.get('start_datetime'):
                    start_datetime = datetime(values['start_datetime'].year, date.today().month, values['start_datetime'].day, values['start_datetime'].hour)
                    values['start_datetime'] = start_datetime
                if values.get('end_datetime'):
                    end_datetime = datetime(values['end_datetime'].year, date.today().month, values['end_datetime'].day, values['end_datetime'].hour)
                    values['end_datetime'] = end_datetime
                values['is_published'] = False
                new_slot_values.append(values)
        slots_to_copy.write({'was_copied': True})
        return self.create(new_slot_values)
