# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from .digital_twin import DigitalTwin
from digital_twin_registry.dependencies import MyBaseModel


class DigitalTwinCollection(MyBaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DigitalTwinCollection - a model defined in OpenAPI

        items: The items of this DigitalTwinCollection.
        total_items: The total_items of this DigitalTwinCollection.
        current_page: The current_page of this DigitalTwinCollection.
        total_pages: The total_pages of this DigitalTwinCollection.
        item_count: The item_count of this DigitalTwinCollection.
    """

    items: List[DigitalTwin]
    total_items: Optional[int]
    current_page: Optional[int]
    total_pages: Optional[int]
    item_count: Optional[int]

DigitalTwinCollection.update_forward_refs()
