class ResourceFactoryModule():
    def __init__(self, location, name):
        self._name = name
        self._location = location
       
    def build(self):
        return [
            {
                "azurerm_resource_group": [
                    {
                    "example": [
                        {
                        "location": self._location,
                        "name": self._name
                        }
                    ]
                    }
                ]
            },
        ]

    def outputs(self):
        return self._name