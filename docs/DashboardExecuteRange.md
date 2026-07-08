# DashboardExecuteRange

Time window applied to every module. Either supply an absolute window (`start` and `end`) OR a relative window (`anchor` and `offset`, optionally with `timezone`), not both. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**anchor** | **str** | Anchor expression for a relative range, e.g. &#x60;now&#x60;. | [optional] 
**offset** | **str** | Offset expression for a relative range, e.g. &#x60;-7D&#x60;. | [optional] 
**timezone** | **str** | IANA timezone identifier (defaults to UTC). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


