rm *.log
rm *.png
rm *.html
rm *.xml
robot --listener robotframework_reportportal.listener --variable RP_UUID:"f6ce8bdf-8b1a-4d8c-a2c9-8ed25d29364b" --variable RP_ENDPOINT:"http://localhost:8080" --variable RP_LAUNCH:"Google Smoke Tests" --variable RP_PROJECT:"test_example" ./google-tests