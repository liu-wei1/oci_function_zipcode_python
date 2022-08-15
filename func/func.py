#
# This is a sample script to access a jason file on OCI Object Storage and
# search address with a Japan zipcode.
#
# Parameter: Japan zipcode (One 7-digit number)
# Output:    Address in JSON format
#
# Please note that this sample is supposed to be used as a Demo only!
#
# Copyright (c) 2022, Oracle and/or its affiliates.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#

import io
import os
import json
import sys
import oci.object_storage

from fdk import response

def handler(ctx, data: io.BytesIO=None):
    try:
        body = json.loads(data.getvalue())
        zipcode = body["zipcode"]
    except Exception:
        raise Exception('No zipcode parameter!')

    # Repalce variable bucketName with you own bucket name
    bucketName = "YourBucketName"
    objectName = "zipcode-jp.json"
    resp = get_address(bucketName, objectName, zipcode)
    return response.Response(
        ctx,
        response_data=resp,
        headers={"Content-Type": "application/json"}
    )

def get_address(bucketName, objectName, zipcode):
    signer = oci.auth.signers.get_resource_principals_signer()
    client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    namespace = client.get_namespace().data
    try:
        message = ""
        print("Searching for object " + objectName + " in bucket " + bucketName + " .", flush=True)
        get_obj = client.get_object(namespace, bucketName, objectName)
        if get_obj.status == 200:
            print("Object " + objectName + " was found.", flush=True)
            file_lines = get_obj.data.text.split('\n')

            flg = linenum = 0
            for line in file_lines:
                linenum = linenum + 1
                if zipcode in line:
                    print("Zipcode " + zipcode + " was found.", flush=True)
                    flg = 1
                    break

            if flg == 0:
                message = '{"Message": "Zipcode ' + zipcode + ' Not Found!"}\n'
            else:
                i = linenum - 1
                address = ""
                while i < linenum + 3:
                    address = address + file_lines[i].lstrip()
                    i = i + 1

                message = "{" + address + "}\n"
                print(message, flush=True)
        else:
            print("Object " + objectName + " was not found.", flush=True)
    except Exception as e:
        message = '{"Message": "Failed: ' + str(e.message) + '"}\n'
    return message
