# DashboardExecuteFilters

Optional filter overrides applied to every module. Every field is optional; omitting one means \"no override on that dimension\". 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**list[AnyOfAnyTypeAnyType]**](AnyOfAnyTypeAnyType.md) | Lines to restrict to. Each entry must supply &#x60;id&#x60;, &#x60;name&#x60;, or both; entries that supply neither are rejected. Other Line fields (factory, secondary_name, match) are not used here and are intentionally omitted so generated clients don&#39;t suggest them as inputs.  | [optional] 
**shifts** | **list[int]** |  | [optional] 
**product_ids** | **list[str]** |  | [optional] 
**product_attribute_value_ids** | **list[str]** |  | [optional] 
**scrap_categories** | **list[str]** |  | [optional] 
**states** | [**DashboardExecuteFiltersStates**](DashboardExecuteFiltersStates.md) |  | [optional] 
**custom_intervals** | [**list[DashboardExecuteFiltersCustomIntervals]**](DashboardExecuteFiltersCustomIntervals.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


