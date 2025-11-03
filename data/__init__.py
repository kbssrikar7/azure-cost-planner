"""
Data module for Azure price catalog and API integration.
"""

from .prices import (
    get_hourly_price,
    get_all_regions_for_vm,
    format_region_name,
    AVAILABLE_REGIONS,
    AVAILABLE_VM_SIZES,
)

__all__ = [
    "get_hourly_price",
    "get_all_regions_for_vm",
    "format_region_name",
    "AVAILABLE_REGIONS",
    "AVAILABLE_VM_SIZES",
]

