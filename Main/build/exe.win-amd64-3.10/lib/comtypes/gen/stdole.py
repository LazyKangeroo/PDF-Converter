from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    Library, VARIANT_BOOL, HRESULT, Picture, DISPPROPERTY, FONTBOLD,
    Font, Checked, FONTSTRIKETHROUGH, IUnknown, _lcid, DISPMETHOD,
    BSTR, OLE_YPOS_CONTAINER, Default, FONTSIZE, OLE_YSIZE_PIXELS,
    OLE_YSIZE_CONTAINER, OLE_XPOS_CONTAINER, Gray, FONTNAME,
    StdPicture, IFontDisp, OLE_XPOS_PIXELS, CoClass, Unchecked,
    OLE_YSIZE_HIMETRIC, Color, _check_version, OLE_XPOS_HIMETRIC,
    OLE_OPTEXCLUSIVE, COMMETHOD, IPicture, StdFont, typelib_path,
    OLE_XSIZE_HIMETRIC, IFontEventsDisp, IFont, OLE_XSIZE_PIXELS,
    OLE_COLOR, IPictureDisp, FONTITALIC, OLE_ENABLEDEFAULTBOOL,
    VgaColor, dispid, Monochrome, OLE_YPOS_PIXELS, IDispatch,
    FONTUNDERSCORE, GUID, OLE_CANCELBOOL, EXCEPINFO,
    OLE_YPOS_HIMETRIC, DISPPARAMS, FontEvents, IEnumVARIANT,
    OLE_HANDLE, OLE_XSIZE_CONTAINER
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'Library', 'IPicture', 'Picture', 'StdFont', 'typelib_path',
    'FONTBOLD', 'OLE_XSIZE_HIMETRIC', 'Font', 'Checked',
    'OLE_XSIZE_PIXELS', 'IFontEventsDisp', 'FONTSTRIKETHROUGH',
    'IFont', 'OLE_COLOR', 'IPictureDisp', 'LoadPictureConstants',
    'FONTITALIC', 'OLE_YPOS_CONTAINER', 'Default', 'FONTSIZE',
    'OLE_ENABLEDEFAULTBOOL', 'VgaColor', 'OLE_YSIZE_PIXELS',
    'OLE_YSIZE_CONTAINER', 'OLE_XPOS_CONTAINER', 'Gray',
    'OLE_TRISTATE', 'Monochrome', 'FONTNAME', 'StdPicture',
    'OLE_YPOS_PIXELS', 'IFontDisp', 'OLE_XPOS_PIXELS',
    'FONTUNDERSCORE', 'Unchecked', 'OLE_YSIZE_HIMETRIC',
    'OLE_CANCELBOOL', 'Color', 'OLE_YPOS_HIMETRIC', 'FontEvents',
    'OLE_XPOS_HIMETRIC', 'OLE_OPTEXCLUSIVE', 'OLE_HANDLE',
    'OLE_XSIZE_CONTAINER'
]

