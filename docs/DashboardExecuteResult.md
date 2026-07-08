# DashboardExecuteResult

Executed output of a single dashboard module.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **str** |  | 
**module_name** | **str** |  | 
**module_type** | **str** | The module&#39;s stored visualization (e.g. &#x60;table&#x60;, &#x60;line_chart&#x60;, &#x60;bar_chart&#x60;). Type label only — does not change the response shape.  | 
**range** | [**DashboardExecuteResultRange**](DashboardExecuteResultRange.md) |  | [optional] 
**filters_applied** | **dict(str, object)** | Echo of the filter dimensions that were applied, resolved to human-readable values where possible (e.g. line names instead of IDs).  | [optional] 
**columns** | [**list[DashboardColumnSpec]**](DashboardColumnSpec.md) | Column metadata. &#x60;type&#x60; is derived from the first non-null cell in the column. Null when the module errored.  | [optional] 
**rows** | **list[dict(str, object)]** | Row data as objects keyed by column name (not positional arrays). Values are typed JSON natively. Null when the module errored.  | [optional] 
**error** | **str** | Set to a short message when the module failed to parse or execute. Null on success.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


