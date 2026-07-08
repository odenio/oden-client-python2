# ScrapYieldData

An object representing scrap and yield data for a line for a particular run or batch interval. Data can be sent unstructured in the `raw_data` field as long as we have a scrap/yield schema for the factory. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_data** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**schema** | [**ScrapYieldSchema**](ScrapYieldSchema.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


