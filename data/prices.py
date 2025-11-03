"""
Internal price catalog for Azure Virtual Machines.
Illustrative prices only — replace with real Azure values or API later.
"""

# Price catalog: prices[region][vm_size][os] = hourly_price
prices = {
    "southindia": {
        "Standard_B1s": {"Linux": 0.012, "Windows": 0.022},
        "Standard_B2s": {"Linux": 0.024, "Windows": 0.034},
        "Standard_D2s_v5": {"Linux": 0.080, "Windows": 0.120},
        "Standard_D4s_v5": {"Linux": 0.160, "Windows": 0.240},
        "Standard_E2s_v5": {"Linux": 0.095, "Windows": 0.135},
        "Standard_F2s_v2": {"Linux": 0.072, "Windows": 0.112},
    },
    "centralindia": {
        "Standard_B1s": {"Linux": 0.013, "Windows": 0.023},
        "Standard_B2s": {"Linux": 0.025, "Windows": 0.035},
        "Standard_D2s_v5": {"Linux": 0.082, "Windows": 0.122},
        "Standard_D4s_v5": {"Linux": 0.164, "Windows": 0.244},
        "Standard_E2s_v5": {"Linux": 0.097, "Windows": 0.137},
        "Standard_F2s_v2": {"Linux": 0.074, "Windows": 0.114},
    },
    "eastus": {
        "Standard_B1s": {"Linux": 0.011, "Windows": 0.021},
        "Standard_B2s": {"Linux": 0.023, "Windows": 0.033},
        "Standard_D2s_v5": {"Linux": 0.078, "Windows": 0.118},
        "Standard_D4s_v5": {"Linux": 0.156, "Windows": 0.236},
        "Standard_E2s_v5": {"Linux": 0.093, "Windows": 0.133},
        "Standard_F2s_v2": {"Linux": 0.070, "Windows": 0.110},
    },
    "westeurope": {
        "Standard_B1s": {"Linux": 0.013, "Windows": 0.023},
        "Standard_B2s": {"Linux": 0.025, "Windows": 0.035},
        "Standard_D2s_v5": {"Linux": 0.084, "Windows": 0.124},
        "Standard_D4s_v5": {"Linux": 0.168, "Windows": 0.248},
        "Standard_E2s_v5": {"Linux": 0.099, "Windows": 0.139},
        "Standard_F2s_v2": {"Linux": 0.076, "Windows": 0.116},
    },
    "southeastasia": {
        "Standard_B1s": {"Linux": 0.012, "Windows": 0.022},
        "Standard_B2s": {"Linux": 0.024, "Windows": 0.034},
        "Standard_D2s_v5": {"Linux": 0.081, "Windows": 0.121},
        "Standard_D4s_v5": {"Linux": 0.162, "Windows": 0.242},
        "Standard_E2s_v5": {"Linux": 0.096, "Windows": 0.136},
        "Standard_F2s_v2": {"Linux": 0.073, "Windows": 0.113},
    },
}

# Available regions in the catalog
AVAILABLE_REGIONS = list(prices.keys())

# Available VM sizes (assuming same sizes available across all regions)
AVAILABLE_VM_SIZES = list(prices["southindia"].keys()) if prices else []


def get_hourly_price(region: str, vm_size: str, os: str) -> float | None:
    """
    Get hourly price for a specific VM configuration.
    
    Args:
        region: Azure region (e.g., "southindia", "eastus")
        vm_size: VM size (e.g., "Standard_D2s_v5")
        os: Operating system ("Linux" or "Windows")
    
    Returns:
        Hourly price as float, or None if not found
    """
    try:
        return prices.get(region, {}).get(vm_size, {}).get(os)
    except (KeyError, AttributeError):
        return None


def get_all_regions_for_vm(vm_size: str, os: str) -> dict[str, float]:
    """
    Get hourly prices for a VM size and OS across all regions.
    
    Args:
        vm_size: VM size (e.g., "Standard_D2s_v5")
        os: Operating system ("Linux" or "Windows")
    
    Returns:
        Dictionary mapping region -> hourly_price
    """
    result = {}
    for region in AVAILABLE_REGIONS:
        price = get_hourly_price(region, vm_size, os)
        if price is not None:
            result[region] = price
    return result


def format_region_name(region: str) -> str:
    """
    Format region code to a more readable name.
    
    Args:
        region: Region code (e.g., "southindia")
    
    Returns:
        Formatted region name (e.g., "South India")
    """
    # Simple formatting: capitalize words
    return region.replace("india", " India").replace("us", " US").replace("europe", " Europe").replace("asia", " Asia").title()

