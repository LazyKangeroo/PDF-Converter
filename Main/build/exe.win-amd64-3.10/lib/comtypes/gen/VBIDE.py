from enum import IntFlag

import comtypes.gen._0002E157_0000_0000_C000_000000000046_0_5_3 as __wrapper_module__
from comtypes.gen._0002E157_0000_0000_C000_000000000046_0_5_3 import (
    _Properties, vbext_wt_FindReplace, vbext_wt_PropertyWindow,
    VBComponent, Library, vbextFileTypeBinary, VARIANT_BOOL, HRESULT,
    _VBProjectsEvents, vbext_wt_CodeWindow, _AddIns,
    _VBComponentsEvents, vbext_wt_Locals, ProjectTemplate, IUnknown,
    _lcid, vbextFileTypePropertyPage, DISPMETHOD,
    vbextFileTypeDocObject, vbext_pk_Proc, vbext_rk_Project,
    Reference, References, _References, vbext_pt_StandAlone,
    vbextFileTypeRes, _dispVBComponentsEvents, CodeModule, CodePane,
    vbext_rk_TypeLib, vbext_ws_Maximize, BSTR, _CodeModule,
    _VBProjects_Old, vbextFileTypeForm, vbext_ws_Minimize,
    vbext_pk_Get, vbextFileTypeFrx, vbextFileTypeModule, AddIn,
    vbext_wt_Find, _dispCommandBarControlEvents, vbext_pk_Set,
    Property, Events, _VBProject_Old, Properties, VARIANT, CoClass,
    vbextFileTypeDesigners, VBProjects, _check_version,
    vbext_wt_LinkedWindowFrame, VBProject, _Components,
    vbext_ws_Normal, _VBProject, vbext_ct_ActiveXDesigner,
    vbext_pp_none, _dispReferencesEvents, Components, _CodePane,
    vbextFileTypeClass, vbextFileTypeUserControl, COMMETHOD,
    vbextFileTypeGroupProject, vbext_ct_MSForm, LinkedWindows,
    vbext_wt_ProjectWindow, vbext_wt_Immediate, _ProjectTemplate,
    vbext_vm_Run, _Windows, _VBComponents, typelib_path,
    _ReferencesEvents, vbext_pk_Let, vbext_vm_Break, VBComponents,
    _dispReferences_Events, _VBComponent_Old, vbext_wt_Browser,
    vbext_wt_Watch, vbext_ct_ClassModule, vbext_ct_Document,
    CommandBarEvents, Window, vbext_pt_HostProject, Addins,
    vbext_vm_Design, _Component, vbext_pp_locked,
    vbextFileTypeProject, CodePanes, dispid, _VBComponents_Old,
    _VBComponent, Component, IDispatch, Windows, _VBProjects,
    vbextFileTypeExe, GUID, SelectedComponents,
    _CommandBarControlEvents, ReferencesEvents, _LinkedWindows,
    _CodePanes, vbext_ct_StdModule, vbext_wt_Toolbox,
    vbext_cv_ProcedureView, VBE, vbext_wt_MainWindow,
    vbext_wt_ToolWindow, _dispVBProjectsEvents, _Windows_old,
    vbext_cv_FullModuleView, Application, vbext_wt_Designer
)


class vbext_VBAMode(IntFlag):
    vbext_vm_Run = 0
    vbext_vm_Break = 1
    vbext_vm_Design = 2


class vbext_ComponentType(IntFlag):
    vbext_ct_StdModule = 1
    vbext_ct_ClassModule = 2
    vbext_ct_MSForm = 3
    vbext_ct_ActiveXDesigner = 11
    vbext_ct_Document = 100


class vbext_ProjectProtection(IntFlag):
    vbext_pp_none = 0
    vbext_pp_locked = 1


class vbext_RefKind(IntFlag):
    vbext_rk_TypeLib = 0
    vbext_rk_Project = 1


class vbext_ProjectType(IntFlag):
    vbext_pt_HostProject = 100
    vbext_pt_StandAlone = 101


class vbext_WindowType(IntFlag):
    vbext_wt_CodeWindow = 0
    vbext_wt_Designer = 1
    vbext_wt_Browser = 2
    vbext_wt_Watch = 3
    vbext_wt_Locals = 4
    vbext_wt_Immediate = 5
    vbext_wt_ProjectWindow = 6
    vbext_wt_PropertyWindow = 7
    vbext_wt_Find = 8
    vbext_wt_FindReplace = 9
    vbext_wt_Toolbox = 10
    vbext_wt_LinkedWindowFrame = 11
    vbext_wt_MainWindow = 12
    vbext_wt_ToolWindow = 15


class vbext_ProcKind(IntFlag):
    vbext_pk_Proc = 0
    vbext_pk_Let = 1
    vbext_pk_Set = 2
    vbext_pk_Get = 3


class vbextFileTypes(IntFlag):
    vbextFileTypeForm = 0
    vbextFileTypeModule = 1
    vbextFileTypeClass = 2
    vbextFileTypeProject = 3
    vbextFileTypeExe = 4
    vbextFileTypeFrx = 5
    vbextFileTypeRes = 6
    vbextFileTypeUserControl = 7
    vbextFileTypePropertyPage = 8
    vbextFileTypeDocObject = 9
    vbextFileTypeBinary = 10
    vbextFileTypeGroupProject = 11
    vbextFileTypeDesigners = 12


class vbext_CodePaneview(IntFlag):
    vbext_cv_ProcedureView = 0
    vbext_cv_FullModuleView = 1


class vbext_WindowState(IntFlag):
    vbext_ws_Normal = 0
    vbext_ws_Minimize = 1
    vbext_ws_Maximize = 2


__all__ = [
    '_Properties', 'vbext_ProjectProtection',
    'vbext_wt_PropertyWindow', 'VBComponent', 'vbextFileTypeBinary',
    '_VBProjectsEvents', '_AddIns', 'vbext_wt_Locals',
    'vbext_RefKind', 'vbextFileTypeDocObject', 'vbext_rk_Project',
    'Reference', '_dispVBComponentsEvents', 'CodePane',
    'vbext_ws_Maximize', '_CodeModule', '_VBProjects_Old',
    'vbext_pk_Get', 'vbextFileTypeFrx', 'vbext_wt_Find',
    '_dispCommandBarControlEvents', 'vbext_pk_Set', 'Events',
    '_VBProject_Old', 'Properties', 'VBProjects',
    'vbext_wt_LinkedWindowFrame', '_Components', 'vbext_ws_Normal',
    '_VBProject', 'Components', 'vbextFileTypeUserControl',
    'vbext_wt_ProjectWindow', '_ProjectTemplate', 'typelib_path',
    'vbext_pk_Let', 'vbext_vm_Break', 'VBComponents',
    '_dispReferences_Events', '_VBComponent_Old', 'vbext_wt_Browser',
    'vbext_wt_Watch', 'vbext_ct_Document', 'vbext_CodePaneview',
    'vbext_vm_Design', 'vbextFileTypeProject', 'vbext_ProcKind',
    '_VBComponents_Old', 'Windows', 'SelectedComponents',
    '_LinkedWindows', '_CodePanes', 'vbext_cv_ProcedureView', 'VBE',
    'vbext_wt_Designer', 'vbext_wt_FindReplace', 'Library',
    'vbext_wt_CodeWindow', '_VBComponentsEvents', 'vbext_WindowType',
    'vbext_WindowState', 'ProjectTemplate',
    'vbextFileTypePropertyPage', 'vbext_pk_Proc', 'References',
    '_References', 'vbext_pt_StandAlone', 'vbextFileTypeRes',
    'CodeModule', 'vbext_rk_TypeLib', 'vbextFileTypeForm',
    'vbext_ws_Minimize', 'vbextFileTypeModule', 'vbext_ComponentType',
    'AddIn', 'Property', 'vbextFileTypes', 'vbextFileTypeDesigners',
    'VBProject', 'vbext_ct_ActiveXDesigner', 'vbext_pp_none',
    '_dispReferencesEvents', '_CodePane', 'vbextFileTypeClass',
    'vbextFileTypeGroupProject', 'vbext_ct_MSForm', 'LinkedWindows',
    'vbext_wt_Immediate', 'vbext_vm_Run', '_Windows', '_VBComponents',
    '_ReferencesEvents', 'vbext_ct_ClassModule', 'CommandBarEvents',
    'vbext_ProjectType', 'Window', 'vbext_VBAMode', 'Addins',
    '_Component', 'vbext_pp_locked', 'CodePanes', '_VBComponent',
    'Component', '_VBProjects', 'vbextFileTypeExe',
    '_CommandBarControlEvents', 'ReferencesEvents',
    'vbext_ct_StdModule', 'vbext_wt_Toolbox', 'vbext_wt_MainWindow',
    'vbext_wt_ToolWindow', '_dispVBProjectsEvents', '_Windows_old',
    'vbext_cv_FullModuleView', 'Application', 'vbext_pt_HostProject'
]

