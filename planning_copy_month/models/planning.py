from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class InheritPlanningSlot(models.Model):
    _inherit = 'planning.slot'

    @api.model
    def action_copy_previous_month(self, date_end_month):

        last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)

        start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

        # For printing results
        print("First day of prev month:", start_day_of_prev_month)
        print("Last day of prev month:", last_day_of_prev_month)
        domain = [
            ('start_datetime', '>=', start_day_of_prev_month),
            ('end_datetime', '<=', last_day_of_prev_month),
            ('recurrency_id', '=', False),
            ('was_copied', '=', False)
        ]
        slots_to_copy = self.search(domain)
        print(slots_to_copy)

        new_slot_values = []
        for slot in slots_to_copy:
            if not slot.was_copied:
                values = slot.copy_data()[0]
                if values.get('start_datetime'):
                    start_datetime = datetime(values['start_datetime'].year, date.today().month, values['start_datetime'].day, values['start_datetime'].hour, values['start_datetime'].minute, values['start_datetime'].second)
                    values['start_datetime'] = start_datetime
                if values.get('end_datetime'):
                    end_datetime = datetime(values['end_datetime'].year, date.today().month, values['end_datetime'].day, values['end_datetime'].hour, values['end_datetime'].minute, values['end_datetime'].second)
                    values['end_datetime'] = end_datetime
                values['is_published'] = False
                new_slot_values.append(values)
        slots_to_copy.write({'was_copied': True})
        return self.create(new_slot_values)
