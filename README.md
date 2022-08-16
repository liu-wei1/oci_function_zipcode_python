# oci_function_zipcode_python

## Source Files
__1. Function Script__
- Name: `func.py`, `func.yaml`, `requirements.txt`

__2. Shell script__
- Name: `call_func_zipcode.sh`
- Parameter: Japan Zipcode (One 7-digit number)
- Location: the client from where you want to call function via API Gateway Endpoint

__3. JSON File__
- Name: `zipcode-jp.json`
- Encode: UTF-8
- Location: OCI Object Storage

## How to invoke
__1. From OCI Cloud Shell or Oracle Linux client__
- Command: call_oci_func_zipcode.sh <JP_Zipcode>
- Example: `call_oci_func_zipcode.sh 1070061`
- Output: `{"zipcode": "1070061","address1": "東京都","address2": "港区","address3": "北青山"}`

__2. From Windows PowerShell__ (Enclose arguments in SINGLE quotes)
- Command: `curl.exe -k -X GET https://<Endpoint_URL> -d '{\"zipcode\": \"1070061\"}'`

__3. From Windows Command Prompt__ (Enclose arguments in DOUBLE quotes)
- Command: `curl -k -X GET https://<Endpoint_URL> -d "{\"zipcode\": \"1070061\"}"`

__4. From the client that the OCI function is created__
- Command: `echo -n '{"zipcode":"1070061"}' | fn invoke <App_Name> <Func_Name>`
