# BMO IL Trade History Importer

for <adjustedcostbase.ca>

## Run

```bash
python3 transform.py [input_file] [output_file] --commission [price]
```

## Data

### Input Data

Export transcation history (trade only) from BMO IL. As of today, this is the current format.

| Column name          | Column number |
| -------------------- | ------------- |
| Transaction Date     | A             |
| Settlement Date      | B             |
| Activity Description | C             |
| Description          | D             |
| Symbol               | E             |
| Quantity             | F             |
| Price                | G             |
| Currency             | H             |
| Total Amount         | I             |
| Currency             | J             |


### Output Data

Go to import tool, and config column mapping with the table below.

| Column name                     | Column number |
| ------------------------------- | ------------- |
| Date                            | A             |
| Security                        | B             |
| Transaction Type                | C             |
| Amount                          | D             |
| Shares                          | E             |
| Commission                      | F             |
| Exchange Rate                   | G             |
| Total or Per Share              | H             |
| Price in Foreign Currency?      | I             |
| Commission in Foreign Currency? | J             |
