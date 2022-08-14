#!/usr/bin/sh
# Purpose: Call OCI Function via API Gateway to access Object Storage
# Prepare: Replace string "endpoint_url" with your own endpoint URL.
#
# Parameter: Japan zip code (One 7-digit number)
# Example:   call_oci_func_zipcode.sh 1070061
# Output:    Address in JSON format
#
# Copyright (c) 2022, Oracle and/or its affiliates.  All rights reserved.
# Licensed under the Universal Permissive License (UPL) Version 1.0 as shown at https://oss.oracle.com/licenses/upl.

if [ $# -ne 1 ];
then	
    echo "Please input one parameter for the Japan zip code you want to search!" 
    exit 1
fi

echo $1 | grep "^[0-9][0-9][0-9][0-9][0-9][0-9][0-9]$" > /dev/null
if [ $? -ne 0 ];
then
    echo "The parameter (Japan zip code) must be a 7-digit number. Please try again."
    exit 1
else
    zipcode=$1
fi

json_string="'""{\"zipcode\": \"$zipcode\"}""'"
echo "---------------------------------------"
echo "CURL command:"

# URL Format: https://<OCID>.apigateway.<region_key>.oci.customer-oci.com/<path_prefix>/<path>"
endpoint_url="https://<OCID>.apigateway.ap-tokyo-1.oci.customer-oci.com/v1/zipcode"
curl_cmd="curl -k -X GET $endpoint_url -d "
echo ${curl_cmd} ${json_string}

echo
echo "---------------------------------------"
echo `date +"%H:%M:%S.%3N"` " - Begin invoke function."
${curl_cmd} '{"zipcode": "'$zipcode'"}'
echo `date +"%H:%M:%S.%3N"` " - End."
echo "---------------------------------------"
