%title: Filepicker demo
%author: slawomir@filepicker.com
%date: 2015-02-24

-> Filepicker <-
=========

-> Connect, store, and process any file from anywhere on the internet. <-

*_Features_*

* Ingestion
* Store
* Processing
* Security
* Custom Providers

-------------------------------------------------

-> # Demo -  Online PDF Viewer <-

-------------------------------------------------

-> Ingestion <-
=========
- Providers
- JavaScript API
 - pick
 - pickAndStore
 - export
 - widgets
 - internationalization
- REST API
- Custom Auth

-------------------------------------------------

-> Providers <-
=========
* Computer
* Box
* Dropbox
* Evernote
* Facebook
* Gmail
* Image Search
* Ftp
* Github
* Google Drive
* Microsoft OneDrive
* Picasa
* Url
* Webcam
* Instagram
* Flickr
* Video
* Alfresco
* Custom Source (S3)
* Amazon Cloud Drive
* CloudApp

-------------------------------------------------

-> JavaScript API: pick <-
=========

As simple as:

    1  filepicker.pick(
    2    function(Blob){
    3      console.log(Blob.url);
    4    }
    5  );

Or even shorter:

    <input type="filepicker" name="My_File" />

-------------------------------------------------

-> JavaScript API: pickAndStore  <-
=========

    1  filepicker.pickAndStore({},{},function(Blobs){
    2    console.log(JSON.stringify(Blobs));
    3  });


-------------------------------------------------

-> JavaScript API: export  <-
=========


    1 filepicker.exportFile(
    2   'https://some.url',
    3     {
    4       mimetype:'image/png'
    5	  },
    6     function(Blob){
    7       console.log(Blob.url);
    8     }
    9  );

-------------------------------------------------


-> JavaScript API: widgets  <-
=========

* Pick Widget

    <input type="filepicker" name="My_File" />

* Drag Drop Widget

    <input type="filepicker-dragdrop" data-fp-multiple="true"/>

* Download Widget

    <button
        data-fp-mimetype="image/png"
        data-fp-url="http://www.filepicker.io/static/img/success.png">
    Save File</button>


-------------------------------------------------

-> Internationalization  <-
=========

Supported languages:

* English: 'en'
* Dutch: 'nl'
* French: 'fr'
* German: 'de'
* Italian: 'it'
* Norwegian: 'no'
* Polish: 'pl'
* Portuguese: 'pt'
* Russian: 'ru'
* Spanish: 'es'
* Turkish: 'tr'
* Chinese (Taiwan): 'zh_tw'

-------------------------------------------------

-> REST API <-
=========

    curl -X POST
         -F fileUpload=@filename.txt
         https://www.filepicker.io/api/store/S3?key=MY_API_KEY

-------------------------------------------------

-> Custom Auth <-
=========

Customer can you his own Cloud applications:

* Alfresco
* Box
* Dropbox
* Evernote
* Facebook
* Flickr
* Google Drive
* Google Search
* Github
* Gmail
* Instagram
* Picasa
* OneDrive

-------------------------------------------------

-> Store <-
=========

Customer can store his files in following storage providers:

* Amazon S3
* Dropbox
* Azure
* Rackspace

-------------------------------------------------

-> Processing <-
=========

* Image conversions
* PDF conversions
* Video encoding

-------------------------------------------------

-> Security <-
=========

- Security Policies

The policies define what the user can and cannot do.
These are time based, where you set an expiration date, and not single use

-------------------------------------------------

-> Custom Providers <-
=========

- Custom Provider SDK
- Custom Conversion SDK
