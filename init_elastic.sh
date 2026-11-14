#!/bin/bash
curl -X POST "http://localhost:9200/articulos/_bulk" -H 'Content-Type: application/json' --data-binary '
{"index":{"_id":"1"}}
{"titulo":"E","precio":2.71}
{"index":{"_id":"2"}}
{"titulo":"Apple Pi","precio":3.14}
'
