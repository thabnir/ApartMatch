curl 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post' \
  -H 'authority: api2.realtor.ca' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.7' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'origin: https://www.realtor.ca' \
  -H 'pragma: no-cache' \
  -H 'referer: https://www.realtor.ca/' \
  -H 'sec-ch-ua: "Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
  --data-raw 'ZoomLevel=10&LatitudeMax=45.75000&LongitudeMax=-72.90380&LatitudeMin=45.36538&LongitudeMin=-74.54213&Sort=6-D&PropertyTypeGroupID=1&TransactionTypeId=3&PropertySearchTypeId=0&Currency=CAD&RecordsPerPage=12&ApplicationId=1&CultureId=1&Version=7.0&CurrentPage=1' \
  | jq