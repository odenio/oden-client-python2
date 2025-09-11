# Interval

An object representing an interval of time on a line and associated metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**IntervalType**](IntervalType.md) |  | 
**name** | **str** |  | [optional] 
**line** | [**Line**](Line.md) |  | 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**metadata** | [**OneOfBatchMetadataRunMetadataStateMetadataobject**](OneOfBatchMetadataRunMetadataStateMetadataobject.md) | Metadata about this interval, such as the associated run or the state category. Will differ based on the type of interval.  | [optional] 
**match** | [**Match**](Match.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


