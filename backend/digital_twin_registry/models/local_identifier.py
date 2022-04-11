# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from digital_twin_registry.dependencies import MyBaseModel


class LocalIdentifier(MyBaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LocalIdentifier - a model defined in OpenAPI

        key: The key of this LocalIdentifier.
        value: The value of this LocalIdentifier.
    """

    key: str
    value: str

LocalIdentifier.update_forward_refs()