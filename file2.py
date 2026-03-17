####Practical 01
Aim: Define a simple service like converting Rupees into Dollars and call it from different platform like JAVA and .NET



Software Tools Required:
•	Code Editor: VS code
•	API Testing Software Application: Postman
•	Framework: Express.js
•	Runtime Environment: Node.js
•	Programming language: JavaScript, Java, C#
Downloads Required:
•	Node.js
•	JDK (Download JDK latest version or higher version than 11.0)
•	.NET SDK
•	Postman
step-1 :- 
go to file explorer --->c:drive--->program files---nodejs (copy this path)
step-2:-
go to edit the system environment variables--->environment variable--->user variable--->click on "PATH"-->edit--->new and paste the path that we have copy--->OK
step-3 :- 
go to file explorer --->c:drive--->program files---dotnet (copy this path) 
step-4:-
go to edit the system environment variables--->environment variable--->user variable--->click on "PATH"-->edit--->new and paste the path that we have copy--->OK
step-5 :- 
go to file explorer --->c:drive--->program files---Eclipse Adoptium--->jsd-11.0.29.7-hotspot-->bin (copy this path)
step-6:-
go to edit the system environment variables--->environment variable--->user variable--->click on "PATH"-->edit--->new and paste the path that we have copy--->OK
then in same System vaiables--->new--->Variable name:-JAVA_HOME-->variable value:- paste the path that we copy--->OK
then in same system vaiable-->CLICK ON PATH--->add this path-->%JAVA_HOME%\bin--->OK

step-7 :- open cmd-->node -v
                     dotnet --version
                     java --version (the version should be higher than 11)
step-8 :- create folder on desktop-->Pr1--->open this folder using vs studio
step-9 :- inside "Pr1"--> create a new folder name it--->currency-conversion-service
step-10 :- inside "currency-conversion-service" folder--->create a file "service.js"

services.js:-(this is for rs-->usd conversion)
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;
app.use(bodyParser.json());
app.post('/convert', (req, res) => {
    const amountInRs = req.body.amount_in_rs;
    const conversionRate = 0.0145;
    const amountInUsd = amountInRs * conversionRate;
    res.json({ amount_in_usd: amountInUsd });
});
app.listen(port, () => {
    console.log(`Currency conversion service running on http://localhost:${port}`);
});

        (OR)
services.js:-(for both conversion)
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// INR → USD
app.post('/convertToUSD', (req, res) => {
    const amountInRs = req.body.amount_in_rs;
    const conversionRate = 0.0145;

    const amountInUsd = amountInRs * conversionRate;

    res.json({ amount_in_usd: amountInUsd });
});

// USD → INR
app.post('/convertToINR', (req, res) => {
    const amountInUsd = req.body.amount_in_usd;
    const conversionRate = 0.0145;

    const amountInRs = amountInUsd / conversionRate;

    res.json({ amount_in_rs: amountInRs });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});

       (OR)
Kilometer → Meter :-
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/convert', (req, res) => {
    const km = req.body.kilometer;

    const meter = km * 1000;

    res.json({ meter: meter });
});

app.listen(port, () => {
    console.log(`KM to Meter service running on http://localhost:${port}`);
});

       (OR)
Kilogram → Gram:-
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/convert', (req, res) => {
    const kg = req.body.kilogram;

    const gram = kg * 1000;

    res.json({ gram: gram });
});

app.listen(port, () => {
    console.log(`KG to Gram service running on http://localhost:${port}`);
});





step-11 :- vs code terminal--->run this--->npm init -y-->npm install express body-parser   --->node services.js

u will get a localhost url--->copy it

step-12 :- open "Postman"-->Select "POST" and paste the localhost url "http://localhost:3000/convert
    In Body:-(write this)
    {
       "amount_in_rs":1000
    }
then click ok "send" button
it will return "amount_in_usd"

step-13 :- again create new folder inside "Pr1" named it "Java_Client"
open it thorugh vs code
install some extension:-(in vs code)
  Java
  Language support for Java(TM) by Red Hat
step-14:- create a file inside a "Java_Client"-->JavaClient.java
write this code:-JavaClient.java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpRequest.BodyPublishers;
import java.net.http.HttpResponse.BodyHandlers;

public class JavaClient {
    public static void main(String[] args) {
        HttpClient client = HttpClient.newHttpClient();
        String uri = "http://localhost:3000/convert";
        String requestBody = "{\"amount_in_rs\":1000}";
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(uri))
                .header("Content-Type", "application/json")
                .POST(BodyPublishers.ofString(requestBody))
                .build();
        client.sendAsync(request, BodyHandlers.ofString())
                .thenApply(HttpResponse::body)
                .thenAccept(System.out::println)
                .join();
    }
}

step-15:- In vs code terminal-->cd (paste the currency-conversion-service path)
                                node service.js
                                this localhost should be running
          then:-(create one more terminal in vs code)
                                javac JavaClient.java
                                java JavaClient
            u will get :- {"amount_in_usd":}
step-16:- create one more folder inside "pr1" named it "NET_Client"
open it thorugh vs code
install some extension:-(in vs code):-
C#Snippets
C#Extensions
C# Dev Kit
C#

in vs code terminal:-dotnet new console
u will get Program.cs file (on left side open it and replace it with ):-
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
class Program
{
    static async Task Main()
    {
        try
        {
            var client = new HttpClient();
            var apiUrl = "http://localhost:3000/convert";

            var requestBody = new
            {
                amount_in_rs = 1000
            };

            var jsonRequestBody = System.Text.Json.JsonSerializer.Serialize(requestBody);

            var response = await client.PostAsync(
                apiUrl,
                new StringContent(jsonRequestBody, Encoding.UTF8, "application/json")
            );

            if (response.IsSuccessStatusCode)
            {
                Console.WriteLine("Response Code: " + response.StatusCode);
                Console.WriteLine("Response Body: " + await response.Content.ReadAsStringAsync());
            }
            else
            {
                Console.WriteLine("Error: " + response.StatusCode);
            }
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine("Error: " + e.Message);
        }
    }
}

again in terminal-->dotnet run (enter)        (but make sure localhost should be running)

✅ Output:
Response Code: OK
Response Body: {"amount_in_usd":14.5}

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

####Practical 02
Aim: Create a simple SOAP service

Note:- pom.xml code will provided in the exam in pr9 folder inside vm.
rest all of the code is to be learnt

Software tools Required:
•	Code Editor: Eclipse IDE
•	Build Automation Tool: Apache Maven
•	SOAP Testing Tool: SOAPUI
•	Framework: Apache CXF
•	Programming Language: Java
Downloads Required:
•	Apache Maven: Download Apache Maven -Maven
•	JDK: java Download | Oracle India
•	Eclipse IDE: Eclipse download
•	SOAP Testing Tool: Download REST & SOAP Automated API testing tools

Step-1 :- go to file explorer-->c:/drive-->apache-maven-3.9.11  (copy this path)
step-2:- go to edit environment varibale-->environment variable-->in system variable-->new-->variable name:MAVEN_HOME-->variable value:(paste the path that u have copy)-->OK

also paste in user variable (PATH) also
also set the java path also
step-3:-open "cmd"--->mvn -v(enter)
                      java --version
step-4:-
Open Eclipse IDE
File → New → Maven Project
in use default workspace location--->click on browse-->go to d:drive/semester 6/ws&ccpracticalperform/practical2--->click on select folder

also tick mark(create a simple program)--->next
In new maven project:-
group id:com.example
artifact id:SimpleSOAPService

then click "FINISH"

step-5:-on left side there is SimpleSOAPService click on down arrow and open pom.xml

replace pom.xml with this:-
<dependencies>

    <!-- Apache CXF -->
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-frontend-jaxws</artifactId>
        <version>3.4.5</version>
    </dependency>

    <!-- HTTP Transport -->
    <dependency>
        <groupId>org.apache.cxf</groupId>
        <artifactId>cxf-rt-transports-http-jetty</artifactId>
        <version>3.4.5</version>
    </dependency>

    <!-- JAX-WS -->
    <dependency>
        <groupId>jakarta.xml.ws</groupId>
        <artifactId>jakarta.xml.ws-api</artifactId>
        <version>2.3.3</version>
    </dependency>

    <!-- Annotation -->
    <dependency>
        <groupId>javax.annotation</groupId>
        <artifactId>javax.annotation-api</artifactId>
        <version>1.3.2</version>
    </dependency>

</dependencies>


     (OR)

< project xmIns="http://maven.apache.org/POM/4.0.0" 
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
http://maven.apache.org/xsd/maven-4.0.0.xsd"> 
<modelVersion>4.0.0</modelVersion>
 <groupId>com.example</groupId>
<artifactld>SimpleSOAPService</artifactid>
<version>0.0.1-SNAPSHOT</version>
<dependencies>
      <!-- Apache CXF for JAX-WS -->
      <dependency>
            <groupId>org.apache.cxf</groupId>
            <artifactId>cxf-rt-frontend-jaxws</artifactld>
            <version> 3.4.5</version>
</dependency>
<! -- Apache CXF HTTP Transport -->
<dependency>
<groupId>org.apache.cxf</groupld>
<artifactId> cxf-rt-transports-http</artifactld>
<version>3.4.5</version>
</dependency>

<! -- Apache CXF HTTP Jetty Transport (for embedded HTTP
server) ->
<dependency>
<groupId>org.apache.cxf</groupId>
<artifactId>exf-rt-transports-http-jetty</artifactId>
< version> 3.4.5</version>
</dependency>

<!-- Jakarta XML WS (JAX-WS API) -->
 <dependency>
      <groupld>jakarta.xml.ws</groupld>
      <artifactId>jakarta.xml.ws-api</artifactId>
      <version >2.3.3</version>
</dependency>

<!-- Java Annotations -->
<dependency>
      <groupld-javax.annotation</groupld> 
      <artifactld>javax.annotation-api</artifactld>
      <version > 1.3.2</version>
    <dependency>
  </dependencies>
</project>

💾 Save (Ctrl + S)

step-6:- on left side inside SimpleSOAPService that is a file "src/main/java" right click on it --->new-->package-->name:com.example-->finish
(com.example will created)
step-7:- right click on-->com.example-->new-->class-->Name:CalculateService.java-->finish
CalculatorService.java:-
package com.example;

import javax.jws.WebMethod;
import javax.jws.WebService;

@WebService
public interface CalculateService {

    @WebMethod
    int add(int num1, int num2);

    @WebMethod
    int subtract(int num1, int num2);
}
step-8:- right click on-->com.example-->new-->class-->Name:CalculatorServiceImpl.java-->finish
CalculatorServiceImpl.java:-
package com.example;

import javax.jws.WebService;

@WebService(endpointInterface = "com.example.CalculatorService")
public class CalculatorServiceImpl implements CalculatorService {

    @Override
    public int add(int num1, int num2) {
        return num1 + num2;
    }

    @Override
    public int subtract(int num1, int num2) {
        return num1 - num2;
    }
}
step-9:-right click on-->com.example-->new-->class-->Name:SOAPServer.java-->finish
SOAPServer.java:-
package com.example;

import javax.xml.ws.Endpoint;

public class SOAPServer {

    public static void main(String[] args) {

        CalculatorServiceImpl implementor = new CalculatorServiceImpl();

        String address = "http://localhost:8080/CalculatorService";

        Endpoint.publish(address, implementor);

        System.out.println("SOAP Service started at " + address);
    }
}

step-10:- 
Right-click → SOAPServer.java
Click → Run As → Java Application
✅ Output:
SOAP Service started at http://localhost:8080/CalculatorService

(copy the localhost url)

step-11:-open SOAPUI
click-->file-->new soap project-->Project Name : CalculatorService-->WSDL URL: http://localhost:8080/CalculatorService?wsdl--->Click OK

step-12:-
Open → add → Request--write this--->
<soapenv:Envelope>
   <soapenv:Body>
      <add>
         <num1>5</num1>
         <num2>2</num2>
      </add>
   </soapenv:Body>
</soapenv:Envelope>

click on run:-

✅ Output:
<addResponse>
   <return>7</return>
</addResponse>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------\
####Practical No :03
Aim: Create a simple REST service

Install:
Python (latest version e.g. 3.12 / 3.13)
VS Code
Postman

Software Tool required:
•	Code Editior : VS code
•	API Testing Software Application : Postman
•	Framework : Flask (micro web framework)

step-1:- Open cmd
    py --version
    pip install flask
(if "pip" is not recognise-->open python file location-->go to script (copy the path) and go to the cmd write cd (paste the path)  or set PATH in environment )

step-2:- Create folder-->foldername:REST_Service-->Open it in VS Code
step-3:- open this folderusing vs code
Install Extensions (VS Code)
Python
Python Debugger
step-4:- Create file--->app.py

app.py:-
from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': data})

# GET item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)

    if item:
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

# POST new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = {
        'id': len(data) + 1,
        'name': request.json['name']
    }
    data.append(new_item)

    return jsonify({
        'message': 'Item added successfully',
        'item': new_item
    }), 201

# Run server
if __name__ == '__main__':
    app.run(debug=True)

     (OR)
from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data
data = [
    {'id': 1, 'name': 'Item 1'},
    {'id': 2, 'name': 'Item 2'}
]

# Endpoint to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': data})

# Endpoint to get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return jsonify({'item': item})
    else:
        return jsonify({'message': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def add_item():
    new_item = {'id': len(data) + 1, 'name': request.json['name']}
    data.append(new_item)
    return jsonify({'message': 'Item added successfully', 'item': new_item}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)   

step-5:- Open terminal in VS Code-->python app.py
✅ Output:
Running on http://127.0.0.1:5000/

STEP 6: Test using Postman
🔹 1. GET All Items
Method → GET
URL:
http://127.0.0.1:5000/items
✅ Output:

{
  "items": [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
  ]
}
🔹 2. GET Item by ID
URL:
http://127.0.0.1:5000/items/1
✅ Output:
{
  "item": {
    "id": 1,
    "name": "Item 1"
  }
}
🔹 3. POST New Item
Method → POST
URL:
http://127.0.0.1:5000/items
Body → raw → JSON:
{
  "name": "Item 3"
}
✅ Output:
{
  "message": "Item added successfully",
  "item": {
    "id": 3,
    "name": "Item 3"
  }
}
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
####Practical No.04

Aim: Develop application to consume Google’s search / Google’s Map RESTful Web Service.

Note:- Apache tomcat zip folder will be present in the vm we need to extract and use it.
index.jsp:
logic will be provide
css file you need to write manually
Api key need to be create inside the exam
make sure to turn off 2 step verification

Install:
JDK (version 11 or higher)
Apache Tomcat (9.0.98)
VS Code / Notepad++

STEP 1: Set Environment Variable
Open → Environment Variables
Click → New User Variable
Variable Name: JAVA_HOME
Variable Value: C:\Program Files\Java\jdk-17

step-2: 
cmd-->java --version

STEP 3: Setup Apache Tomcat
Download Tomcat
Create folder at desktop-->GoogleMaps--->Extract Tomcat inside it

STEP 4: Start Tomcat Server
Go to-->GoogleMaps-->apache-tomcat(Extracted folder)-->bin
Method 1:
👉 Double-click:
startup.bat
Method 2:
startup.bat (via CMD)
✔️ Tomcat runs in background

STEP 5: Create Web Project
Go to-->GoogleMaps-->apache-tomcat-->webapps--->create a folder-->myjsp
open myjsp through vs code

step 6:- inside myjsp-->create a file-->
myindex.jsp:-
<%@ page contentType="text/html; charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head>
<title>Google Maps</title>
</head>

<body>

<h2>Google Map Location</h2>

<%
String lat = request.getParameter("t1");
String lng = request.getParameter("t2");

String defaultLat = "28.6139";
String defaultLng = "77.2090";

if(lat == null || lng == null){
    lat = defaultLat;
    lng = defaultLng;
}
%>

<div id="map" style="height:500px;width:100%;"></div>

<script>
function initMap() {
    var location = { lat: <%=lat%>, lng: <%=lng%> };

    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 10,
        center: location
    });

    var marker = new google.maps.Marker({
        position: location,
        map: map
    });
}
</script>

<!-- Replace YOUR_API_KEY -->
<script async defer
src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap">
</script>

</body>
</html>


       (OR)
'''<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Google Maps Location (Safe)</title>
        <style>
            html,
            body {
                height: 100%;
                margin: 0;
            }

            #map {
                height: 70vh;
                width: 100%;
            }

            .wrap {
                max-width: 960px;
                margin: 0 auto;
                padding: 1rem;
                font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
            }

            .card {
                background: #fff;
                border: 1px solid #e5e7eb;
                border-radius: 12px;
                padding: 1rem;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
            }

            .error {
                color: #b91c1c;
                background: #fee2e2;
                border: 1px solid #fecaca;
                padding: .5rem .75rem;
                border-radius: .5rem;
            }

            .muted {
                color: #6b7280;
                font-size: 0.9rem;
            }
        </style>
        <% String latStr=request.getParameter("t1"); String lngStr=request.getParameter("t2"); Double lat=null; Double
            lng=null; String error=null; try { if (latStr !=null && lngStr !=null && !latStr.trim().isEmpty() &&
            !lngStr.trim().isEmpty()) { lat=Double.valueOf(latStr.trim().replace(',', '.' ));
            lng=Double.valueOf(lngStr.trim().replace(',', '.' )); if (lat < -90 || lat> 90 || lng < -180 || lng> 180) {
                throw new IllegalArgumentException("Coordinates out of range");
                }
                }
                } catch (Exception ex) {
                error = "Invalid coordinates: " + ex.getMessage();
                }

                double defLat = 28.6139; // Default latitude
                double defLng = 77.2090; // Default longitude
                %>

    </head>

    <body>
        <div class="wrap">
            <h1>Google Maps Location</h1>
            <p class="muted">This page reads <code>t1</code> (latitude) and <code>t2</code> (longitude) from the query
                string and centers the map.</p>

            <% if (error !=null) { %>
                <p class="error">
                    <%= error %>. Showing default location instead.
                </p>
                <% } else if (lat==null || lng==null) { %>
                    <p class="muted">Tip: open <code>myinput.jsp</code> and submit coordinates. Example: 28.6139,
                        77.2090</p>
                    <% } %>

                        <div id="map" class="card"></div>

                        <div class="card" style="margin-top:1rem;">
                            <p><strong>Current center:</strong>
                                Lat: <span id="latSpan"></span> ,
                                Lng: <span id="lngSpan"></span>
                            </p>
                        </div>
        </div>

        <script>
            // Values from server (fallback to defaults if missing)
            const serverLat = <%= (lat != null ? lat : defLat) %>;
            const serverLng = <%= (lng != null ? lng : defLng) %>;
            const hasUserInput = <%= (lat != null && lng != null) ? "true" : "false" %>;

            function initMap() {
                const center = { lat: serverLat, lng: serverLng };
                const map = new google.maps.Map(document.getElementById("map"), {
                    center,
                    zoom: hasUserInput ? 14 : 11,
                });
                new google.maps.Marker({ position: center, map });

                // Show the numbers
                document.getElementById("latSpan").textContent = center.lat.toFixed(6);
                document.getElementById("lngSpan").textContent = center.lng.toFixed(6);

                // Allow user to click to move marker and update display (no server roundtrip)
                map.addListener("click", (e) => {
                    const pos = { lat: e.latLng.lat(), lng: e.latLng.lng() };
                    map.setCenter(pos);
                    marker.setPosition(pos);
                    document.getElementById("latSpan").textContent = pos.lat.toFixed(6);
                    document.getElementById("lngSpan").textContent = pos.lng.toFixed(6);
                });
                const marker = new google.maps.Marker({ position: center, map, draggable: true });
                marker.addListener("dragend", () => {
                    const p = marker.getPosition();
                    const pos = { lat: p.lat(), lng: p.lng() };
                    document.getElementById("latSpan").textContent = pos.lat.toFixed(6);
                    document.getElementById("lngSpan").textContent = pos.lng.toFixed(6);
                });
            }
        </script>

        <!-- IMPORTANT: Replace YOUR_API_KEY with your real Google Maps API key.
       Enable the Maps JavaScript API in Google Cloud. -->
        <script async defer
            src="https://maps.googleapis.com/maps/api/js?key=AIzaSyALU5Mx4kXMGv8U--GxWrHvQ4h1EHgpkwc&callback=initMap"></script>
    </body>

    </html>


File 2: myinput.jsp:-
<%@ page contentType="text/html" %>
<!DOCTYPE html>
<html>
<head>
<title>Enter Location</title>
</head>

<body>

<form action="myindex.jsp" method="get">
    Enter Latitude: <input type="text" name="t1"><br><br>
    Enter Longitude: <input type="text" name="t2"><br><br>
    <input type="submit" value="Show Map">
</form>

</body>
</html>

      (OR)
<%@ page contentType="text/html" pageEncoding="UTF-8" %>
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Enter Latitude and Longitude</title>
    </head>
    <body>
        <!-- Form to accept input values for latitude and longitude -->
        <form action="myindex.jsp" method="get">
            <pre>
            Enter latitude: <input type="text" name="t1" />
            Enter longitude: <input type="text" name="t2" />
            <input type="submit" value="Show" />
        </pre>
        </form>
    </body>
    </html>

STEP 7: Run Project
Open browser-->http://localhost:8080/myjsp/myinput.jsp

STEP 8: Enter Coordinates
Example:
Latitude: 19.0760
Longitude: 72.8777
Click:

Show Map
✅ Output:
Google Map opens
Marker shows entered location

api key :- AIzaSyBMQdxZByN9VpjKcwi0oqZzYC_sHwDUi88

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#####Practical No. 05
A: Installation and Configuration of virtualization using KVM.

Note:-vm iso file required for vm creation will be provide

Install:
VMware Workstation
Ubuntu ISO (Linux OS)

STEP 1: Create Virtual Machine (VMware)
Open VMware Workstation
Click:
Create New Virtual Machine
Select:
Installer disc image (ISO)
Browse Ubuntu ISO

| Field     | Value          |
| --------- | -------------- |
| Full Name | WSCCPractical5 |
| Username  | example        |
| Password  | linux          |
| VM Name   | KVM            |
| Disk Size | 20 GB          |

Click Next → Finish

STEP 2: Enable Virtualization
Click:
Edit Virtual Machine Settings
Go to Processor
Tick:
Virtualize Intel VT-x / AMD-V
✔️ Required for KVM

STEP 3: Install Ubuntu
Follow installation steps:
Select Language → Next
Keyboard → English (US)
Connect Internet
Select:
Install Ubuntu
Choose:
Default Installation
Tick:
✔️ Install third-party software
Select:
Erase disk and install Ubuntu
Enter:
Name: Kishore
Password: linux90
Timezone:
Asia/Kolkata
Click:
Install → Restart
✔️ Login after restart

STEP 4: Open Terminal (KVM Setup)
1. Update System
sudo apt update && sudo apt upgrade -y
2. Check Virtualization Support
sudo grep -c "svm\|vmx" /proc/cpuinfo
✔️ Output > 0 → Supported
3.Check KVM Support
kvm-ok
If not found:
sudo apt install cpu-checker
kvm-ok
✅ Expected Output:
INFO: /dev/kvm exists
KVM acceleration can be used
4. Install KVM Packages
sudo apt install qemu-kvm virt-manager libvirt-daemon-system libvirt-clients bridge-utils -y
5. Start KVM Service
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
6. Check Status
sudo systemctl status libvirtd
✔️ Should be active (running)
7. (Optional) Add User to Groups
sudo usermod -aG kvm your-username
sudo usermod -aG libvirt your-username
🔹 8. Logout & Login Again
✔️ Required for changes

STEP 5: Open Virtual Machine Manager
Search:
Virtual Machine Manager
Open it

STEP 6: Create New VM (KVM)
Click:
Create New Virtual Machine
Select OS (Ubuntu/Windows)
Allocate:
RAM
CPU
Enable storage
Click:
Finish

✅ Output:
VM will run inside KVM
Ubuntu screen appears


Note: if error occur:-
* If issue arise with VM in chap 5 for KVM

Step 1: Turn off Hyper-V feature
Open Windows search → Turn Windows feature on/off

→ Uncheck these:
- Hyper-V
- Virtual Machine Platform
- Windows Sandbox
- Windows Subsystem for Linux

Click OK → Restart

Step 2: Disable Hyper-V using CMD
→ bcdedit /set hypervisorlaunchtype off
→ Restart

Step 3: Start VM again
VM → Settings → Processor
Enable Virtualize Intel VT-x/EPT or AMD-V/RVI

Step 4: In Ubuntu
ls /dev/kvm

--- Error Fix ---

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#####Practical No.6
Aim: Develop application to download image/video from server or upload image/video to server using MTOM techniques

Note:-
nothing will provide

Install:
NetBeans IDE (8.0.2 recommended)
JDK 8
GlassFish Server 4.1

step-1:- open netbeans-->click file-->new project-->select "Java web"-->web application-->click Next
Enter details:
Project Name:ImageTransferApp
Click Next → Finish
✔️ GlassFish will be default server

step 2:- go to file explorer-->picture-->create a folder-->name it "upload"-->create another folder--->name it "download"-->Add one image:S2.jpg in picture folder

STEP 3: 
Right-click project-->Click:--->New → Web Service--->Enter:-->Name: ImageWS-->Package:mypkg.ws
Click Finish

step 4:left side inside project--->source packages-->mypkg.ws-->ImageWS.java
ImageWS.java:- 
package mypkg.ws;

import java.io.*;
import javax.jws.*;
import javax.xml.ws.soap.MTOM;

@MTOM(enabled = true, threshold = 60000)
@WebService(serviceName = "ImageWS")
public class ImageWS {

    private static final String PATH = "C:/Users/Amit/Pictures/upload/";

    @WebMethod
    public void upload(String filename, byte[] imageBytes) {
        try (FileOutputStream fos = new FileOutputStream(PATH + filename);
             BufferedOutputStream bos = new BufferedOutputStream(fos)) {

            bos.write(imageBytes);
            bos.flush();

            System.out.println("Uploaded: " + filename);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @WebMethod
    public byte[] download(String filename) {
        try {
            File file = new File(PATH + filename);
            byte[] bytes = new byte[(int) file.length()];

            try (FileInputStream fis = new FileInputStream(file)) {
                fis.read(bytes);
            }

            return bytes;

        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}

                  (OR)
package mypkg.ws;
import java.io.*;
import javax.jws.*;
import javax.xml.ws.soap.MTOM;
@MTOM(enabled = true, threshold = 60000)
@WebService(serviceName = "ImageWS")
public class ImageWS {
    private static final String PATH = "C:/Users/bhoom/Pictures/upload/";
    @WebMethod
    public void upload(
            @WebParam(name = "filename") String filename,
            @WebParam(name = "imageBytes") byte[] imageBytes) {
        try (FileOutputStream fos =
                     new FileOutputStream(PATH + filename);
             BufferedOutputStream bos =
                     new BufferedOutputStream(fos)) {
            bos.write(imageBytes);
            bos.flush();
            System.out.println("Uploaded: " + filename);
            System.out.println("Bytes received: " + imageBytes.length);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    @WebMethod
    public byte[] download(
            @WebParam(name = "filename") String filename) {
        try {
            File file = new File(PATH + filename);
            byte[] bytes = new byte[(int) file.length()];
            try (FileInputStream fis = new FileInputStream(file);
                 BufferedInputStream bis =
                         new BufferedInputStream(fis)) {

                bis.read(bytes);
            }
            System.out.println("Downloaded: " + filename);
            return bytes;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}

step-5:-Right-click project:-->Clean and Build--->Run
it will move on chrome with localhost and visible "TODO write Content"

step-6:-
right click on project --->new--->other-->web services-->web services client-->next-->select project-->imageTranferApps/imageWS-->OK-->package:mypkg.client-->finish
✔️ Client created automatically

step-7:-
Right-click project-->New → JSP--->Name:index.jsp
Add JSP Code:-
<%@page import="java.io.*"%>
<%@page import="javax.xml.ws.soap.MTOMFeature"%>
<%@page import="mypkg.client.*"%>

<h2>Upload Image</h2>

<%
ImageWS_Service service = new ImageWS_Service();
ImageWS port = service.getImageWSPort(new MTOMFeature(60000));

File file = new File("C:/Users/Amit/Pictures/S2.jpg");
byte[] data = new byte[(int) file.length()];

FileInputStream fis = new FileInputStream(file);
fis.read(data);

port.upload(file.getName(), data);
out.println("Uploaded: " + file.getName());

fis.close();
%>

<hr/>

<h2>Download Image</h2>

<%
ImageWS_Service service2 = new ImageWS_Service();
ImageWS port2 = service2.getImageWSPort(new MTOMFeature(60000));

String filename = "S2.jpg";
byte[] data2 = port2.download(filename);

FileOutputStream fos = new FileOutputStream(
"C:/Users/Amit/Pictures/download/" + filename);

fos.write(data2);

out.println("Downloaded: " + filename);

fos.close();
%>

      (OR)
<%-- 
    Document   : index
    Created on : 10 Feb, 2026, 9:38:40 PM
    Author     : bhoom
--%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="java.io.*"%>
<%@page import="javax.xml.ws.soap.MTOMFeature"%>
<%@page import="mypkg.client.*"%>
<!DOCTYPE html>
<html>
<head>
    <title>SOAP Image Upload & Download</title>
</head>
<body>
<h2>Upload Image</h2>
<%
ImageWS_Service service = new ImageWS_Service();
ImageWS port = service.getImageWSPort(new MTOMFeature(60000));
FileInputStream fis = null;
try {
    File file = new File("C:/Users/bhoom/Pictures/book.jpg");
    byte[] data = new byte[(int) file.length()];
    fis = new FileInputStream(file);
    fis.read(data);
    port.upload(file.getName(), data);
    out.println("Uploaded: " + file.getName());
} catch (Exception e) {
    e.printStackTrace();
} finally {
    if (fis != null) fis.close();
}
%>
<hr/>
<h2>Download Image</h2>
<%
FileOutputStream fos = null;
try {
    ImageWS_Service service2 = new ImageWS_Service();
    ImageWS port2 =
            service2.getImageWSPort(new MTOMFeature(60000));
    String filename = "book.jpg";
    byte[] data = port2.download(filename);
    fos = new FileOutputStream(
            "C:/Users/bhoom/Pictures/download/" + filename);
    fos.write(data);
    out.println("Downloaded: " + filename);
} catch (Exception e) {
    e.printStackTrace();
} finally {
    if (fos != null) fos.close();
}
%>
</body>
</html>


step-8:- 
Right-click project--->Clean and Build--->Deploy-->Run--->index.jsp

✅OUTPUT
In browser:
Uploaded: S2.jpg
Downloaded: S2.jpg

-----------------------------------------------------------------------------------------------------------------------------------
Practical No 07
Aim: Implement Platform as a Service (PaaS) by installing and running a Flask web application inside a Lubuntu virtual machine using VirtualBox, with a Python virtual environment and host-based access via the VM’s IP address.

Install:
VirtualBox
Lubuntu ISO file

STEP 2: Create Virtual Machine
Open VirtualBox-->New
Enter details:
Field	  Value
Name	  Lubuntu
Type	  Linux
Version	  Ubuntu (64-bit)

Allocate Resources
RAM → 2 GB or more
Disk → 20 GB

Mount ISO
Go to-->Settings → Storage--->Select empty disk--->Choose Lubuntu ISO

STEP 3: Start VM
Click Start--->Select--->Try Lubuntu
✔️ Opens OS without installation

STEP 4: Open Terminal
sudo apt-get update
sudo mkdir WSCC
cd WSCC
sudo apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate
pip install flask
nano app.py  or sudo nano app.py

Paste code:
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is working!"

@app.route("/about")
def about():
    return "This is About Page!"

if __name__ == "__main__":
    app.run(debug=True)

   (OR)
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask is working!"
@app.route("/about")
def about():
    return "This is About Page!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

Save:
Ctrl + O → Enter → Ctrl + X

Run Flask App:-
python3 app.py

✅ Output:
Running on http://127.0.0.1:5000/
Running on http://<your-ip>:5000/

open in browser
✅ Output:
/ → Hello message
/about → About page


----------------------------------------------------------------------------------------------------------------------------------------------\

Practical 8
Aim: SaaS using Apache.

Install:
XAMPP (Apache Server)
Practical ZIP file (PRAC8)

Step 1: Download practical 8 zip file. Extract zip file. Rename the file name as PRAC8.

Step2: Copy extracted zip file and paste in C driver -> XAMPP -> htdocs

Step 3: In XAMPP server, start Apache.

Step 4: Search ethernet setting. Copy the IPv4 address. Example:192.168.1.5

Step 5: Paste the IP4 address. 

Step 6:  In browser URL, instead of dashboard type PRAC8. You will get the following page.
Open browser:
http://localhost/PRAC8
OR using IP:
http://192.168.1.5/PRAC8

Step 7: Click on tinyfilemanager.php.

Step 8: Enter the username is “admin” and password is “admin@123”. You will get the following page.

Step 9: Click on new Item. Create new folder named as “upload”.

STEP 10: Upload File
Open upload folder
Click-->Upload (top right)
Select any file
✔️ File uploaded successfully

Step 11: After uploading any file you will get that file in list. 

Step 12: If you want to share the file within network to another person then only just type the uploader IP address/foldername. Example: http://192.168.6.192/PRAC8/upload

------------------------------------------------------------------------------------------------------------------------------------
Practical No:9
Aim: To connect a Java application with Amazon Simple Workflow Service (SWF) using AWS SDK and retrieve registered workflow domains.

Step 1: AWS Console Login
1.	Open browser
2.	Go to: https://aws.amazon.com/console/
3.	Login using Root user 
4.	After login then search IAM
 
Step 2: Create IAM User
1.	Go to IAM
2.	Click Users
3.	Click Create User
4.	Enter user name: aws-java-user
5.	Click Next
 
Step 3: Set Permissions
1.	Select Attach policies directly
2.	Search: AdministratorAccess
3.	Select the policy
4.	Click Next
 
Step 4: Review and Create User
1.	Review details
2.	Click Create User
 
Step 5: User Created Successfully
After creation:
1.	Click on created user
2.	Go to Security Credentials
 

Step 6: Create Access Key
1.	Scroll to Access Keys
2.	Click Create Access Key
 
Step 7: Select Use Case
1.	Select: Command Line Interface (CLI)
2.	Click Next
 

Step 8: Create Access Key
1.	Click Create Access Key
2.	Copy Access Key and Copy Secret Access Key OR Click Download .csv file
 
Step 9: Then Download AWSCLI.msi Which is located on WSCC folder
Step 10 : Configure AWS CLI
Open Command Prompt and type: aws configure
Enter:
•	Access Key
•	Secret Key
•	Region: ap-south-1
•	Output format: json
 
Step 11: NetBeans Project Creation Steps
1.	Open Apache NetBeans IDE
2.	Click on File → New Project
3.	Select Maven → Java Application
4.	Enter Project Name as AWSWorkFlow
5.	Click Finish
 
Step 12: Go to Project Files -> pom.xml Configuration
Open pom.xml and add the following dependencies:
if any other version is written, replace it with:
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
</properties>
Add Dependencies Inside the project:
<dependencies>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>swf</artifactId>
        <version>2.25.28</version>
    </dependency>
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-simple</artifactId>
        <version>2.0.9</version>
    </dependency>
</dependencies>

       (OR)
<properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
</properties>

<dependencies>
    <dependency>
        <groupId>software.amazon.awssdk</groupId>
        <artifactId>swf</artifactId>
        <version>2.25.28</version>
    </dependency>

    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-simple</artifactId>
        <version>2.0.9</version>
    </dependency>
</dependencies>



Step 13: Create Class, Right Click on AWSWorkFlow project -> New -> Java Class and give the file name AWSConnect  and Click finish
Java Implementation Code:
import software.amazon.awssdk.services.swf.SwfClient;
import software.amazon.awssdk.services.swf.model.ListDomainsRequest;
import software.amazon.awssdk.services.swf.model.ListDomainsResponse;
import software.amazon.awssdk.regions.Region;
public class AWSConnect {
    public static void main(String[] args) {
        SwfClient swf = SwfClient.builder()
                .region(Region.AP_SOUTH_1)
                .build();
        System.out.println("Connected to AWS SWF!");
        ListDomainsRequest request = ListDomainsRequest.builder()
                .registrationStatus("REGISTERED")
                .build();
        ListDomainsResponse response = swf.listDomains(request);
        System.out.println(response);
    }
}
      (OR)
import software.amazon.awssdk.services.swf.SwfClient;
import software.amazon.awssdk.services.swf.model.ListDomainsRequest;
import software.amazon.awssdk.services.swf.model.ListDomainsResponse;
import software.amazon.awssdk.regions.Region;

public class AWSConnect {
    public static void main(String[] args) {

        SwfClient swf = SwfClient.builder()
                .region(Region.AP_SOUTH_1)
                .build();

        System.out.println("Connected to AWS SWF!");

        ListDomainsRequest request = ListDomainsRequest.builder()
                .registrationStatus("REGISTERED")
                .build();

        ListDomainsResponse response = swf.listDomains(request);

        System.out.println(response);
    }
}

Step 14: Running the Project
Right click on the project in NetBeans and click on Build and Click.
After Success of Build and Click then Right click on the project in NetBeans and click Run.
The application will connect to AWS SWF and display the registered domains.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

PRACTICAL NO. 10 – FULL GUIDE
Aim:-To install OpenStack using DevStack and create user & private network.
STEP 1: Requirements
Hardware:
RAM → 8 GB minimum
CPU → 2 cores
Storage → 50 GB
Software:
Ubuntu Server 22.04
VirtualBox / VMware
DevStack (OpenStack)
STEP 2: Update System
Open terminal:
sudo apt update && sudo apt upgrade -y
STEP 3: Create Stack User
sudo useradd -s /bin/bash -d /opt/stack -m stack
sudo passwd stack
sudo usermod -aG sudo stack
su - stack
✔️ Switch to stack user
📦 STEP 4: Install Git
sudo apt install git -y
⬇️ STEP 5: Download DevStack
git clone https://opendev.org/openstack/devstack
cd devstack
⚙️ STEP 6: Create Configuration File
nano local.conf
Paste:
[[local|localrc]]
ADMIN_PASSWORD=admin
DATABASE_PASSWORD=admin
RABBIT_PASSWORD=admin
SERVICE_PASSWORD=admin
HOST_IP=your_ip_address
👉 Replace:
your_ip_address
▶️ STEP 7: Install OpenStack
./stack.sh
⏳ Takes 15–30 minutes
🔐 STEP 8: Load Credentials
source devstack/openrc
👥 STEP 9: Create User
openstack user create student1 --password student123
openstack role add --project demo --user student1 member
🌐 STEP 10: Create Network
openstack network create private-net
🔹 Create Subnet
openstack subnet create private-subnet \
--network private-net \
--subnet-range 192.168.1.0/24 \
--gateway 192.168.1.1
✔️ STEP 11: Verify Output
openstack user list
openstack network list
openstack subnet list
✔️ Shows created user & network
🌍 STEP 12: Open Dashboard (Horizon)
Open browser:
http://<your-ip>/dashboard
🔐 Login:
Username: admin
Password: admin
👤 STEP 13: Create User via Dashboard

Go to:

Identity → Users → Create User

Enter:

Name → student1

Password → student123

Role → Member

Project → demo

🌐 STEP 14: Create Network via Dashboard

Go to:

Project → Network → Networks → Create Network

Enter:

Network Name → private-net

Subnet → private-subnet

Address → 192.168.1.0/24

Gateway → 192.168.1.1
 






