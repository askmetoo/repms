from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Real Estate"),
        "icon": "octicon octicon-home",
        "items": [
            {
              "type": "doctype",
              "name": "Property",
              "label": _("Property"),
              "description": _("Properties within the real estate portfolio."),
            }
          ]
      }
  ]
