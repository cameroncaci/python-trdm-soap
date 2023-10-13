# Getting xmlsec on MacOS (Apple Silicon Processor)
See workaround: https://github.com/xmlsec/python-xmlsec/issues/254#issuecomment-1507659129

**virtual environment strongly recommended**

## WSDL Service
*Generated from Suds*

**Service**: ReturnTable  

### Prefixes (1)
- ns0 = "http://trdm/ReturnTableService"

### Ports (1)
- ReturnTableWSSoapHttpPort

  #### Methods (2)
  - `getLastTableUpdate(physicalNameType physicalName)`
  - `getTable(ReturnTableInput input)`

  #### Types (38)
  - ReturnTableInput
  - ReturnTableLastUpdateRequest
  - ReturnTableLastUpdateResponse
  - ReturnTableOutput
  - ReturnTableRequestElement
  - ReturnTableResponseElement
  - attribute
  - authorityOrLocationDetailsType
  - column
  - columnFilter
  - columnFilterMatchesCriteria
  - columnFilterTypeAndValues
  - dataAuthorityType
  - dataLocationType
  - dateFilterValue
  - dateTimeFilterValue
  - entitySource
  - filterValue
  - lastUpdate
  - multiValueFilter
  - multiValueFilterType
  - noValueFilter
  - noValueFilterType
  - numericalFilterValue
  - physicalNameType
  - rowNum
  - singleValueDateFilter
  - singleValueDateFilterType
  - singleValueDateTimeFilter
  - singleValueDateTimeFilterType
  - singleValueFilter
  - singleValueFilterType
  - singleValueNumericalFilter
  - singleValueNumericalFilterType
  - status
  - twoValueDateTimeFilter
  - twoValueFilterType
  - twoValueNumericalFilter
