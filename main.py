import json


def hello_server(name, network):
    return {
    "provider": [
        {
        "azurerm": [
            {
            "features": [
                {}
            ]
            }
        ]
        }
    ],
  "resource": [
    {
      "azurerm_resource_group": [
        {
          "example": [
            {
              "location": "West Europe",
              "name": "example-resources"
            }
          ]
        }
      ]
    },
    {
      "azurerm_virtual_network": [
        {
          "example": [
            {
              "address_space": [
                "10.0.0.0/16"
              ],
              "location": "West Europe",
              "name": "example-network",
              "resource_group_name": "example-resources"
            }
          ]
        }
      ]
    },
    {
      "azurerm_subnet": [
        {
          "example": [
            {
              "address_prefixes": [
                "10.0.2.0/24"
              ],
              "name": "internal",
              "resource_group_name": "example-resources",
              "virtual_network_name": "example-network"
            }
          ]
        }
      ]
    },
    {
      "azurerm_network_interface": [
        {
          "example": [
            {
              "ip_configuration": [
                {
                  "name": "internal",
                  "private_ip_address_allocation": "Dynamic"
                }
              ],
              "location": "West Europe",
              "name": "example-nic",
              "resource_group_name": "example-resources"
            }
          ]
        }
      ]
    },
    {
      "azurerm_linux_virtual_machine": [
        {
          "example": [
            {
              "admin_username": "adminuser",
              "network_interface_ids": [
                "${azurerm_network_interface.example.id}"
              ],
              "location": "West Europe",
              "name": "example-machine",
              "os_disk": [
                {
                  "caching": "ReadWrite",
                  "storage_account_type": "Standard_LRS"
                }
              ],
              "resource_group_name": "example-resources",
              "size": "Standard_F2",
              "source_image_reference": [
                {
                  "offer": "UbuntuServer",
                  "publisher": "Canonical",
                  "sku": "16.04-LTS",
                  "version": "latest"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}

if __name__ == "__main__":
    config = hello_server(name='hello-world', network='default')

    with open('main.tf.json', 'w') as outfile:
        json.dump(config, outfile, sort_keys=True, indent=4)