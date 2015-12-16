#retriever

"""Retriever script for direct download of vertnet data"""
from retriever.lib.models import Table
from retriever.lib.templates import Script
import os


class main(Script):
    def __init__(self, **kwargs):
        Script.__init__(self, **kwargs)
        self.name = "vertnet:"
        self.shortname = "vertnet"
        self.ref = "http://vertnet.org/resources/datatoolscode.html"
        self.urls = {
                    'amphibians': 'https://knb.ecoinformatics.org/knb/d1/mn/v1/object/urn:uuid:afc58110-b9c1-4cf7-b46c-837bdc930a21',
                    'birds': 'https://knb.ecoinformatics.org/knb/d1/mn/v1/object/urn:uuid:cca85e21-6647-491c-aa57-89a7c552e564',
                    'fishes': 'https://knb.ecoinformatics.org/knb/d1/mn/v1/object/urn:uuid:74f312ce-de6f-4cae-b5f7-26d4d0ffc781',
                    'mammals': 'https://knb.ecoinformatics.org/knb/d1/mn/v1/object/urn:uuid:1d09e64b-d25a-46e7-bdc1-0a91fb7bf8bb',
                    'reptiles': 'https://knb.ecoinformatics.org/knb/d1/mn/v1/object/urn:uuid:14a66a88-592e-4459-ae8a-b114165106c3'
        }
        self.description = " "
        self.tags = ['Taxon > animals']

    def download(self, engine=None, debug=False):
        Script.download(self, engine, debug)
        engine = self.engine

        file_names = [ ('vertnet_latest_amphibians.csv','amphibians'),
                        ('vertnet_latest_birds.csv','birds'),
                        ('vertnet_latest_fishes.csv','fishes'),
                        ('vertnet_latest_mammals.csv','mammals'),
                        ('vertnet_latest_reptiles.csv','reptiles')
                      ]

        for(filename,tablename) in file_names:

            table = Table(str(tablename) , delimiter=',' )
            # all tables in vertnet data have same field names
            table.columns = [   ("record_id"                              ,   ("pk-auto",)    ),
                                ("beginrecord"                            ,   ("char",)    ),
                                ("icode"                                  ,   ("char",)    ),
                                ("title"                                  ,   ("char",)    ),
                                ("citation"                               ,   ("char",)    ),
                                ("contact"                                ,   ("char",)    ),
                                ("dwca"                                   ,   ("char",)    ),
                                ("email"                                  ,   ("char",)    ),
                                ("eml"                                    ,   ("char",)    ),
                                ("emlrights"                              ,   ("char",)    ),
                                ("gbifdatasetid"                          ,   ("char",)    ),
                                ("gbifpublisherid"                        ,   ("char",)    ),
                                ("iptlicense"                             ,   ("char",)    ),
                                ("migrator"                               ,   ("char",)    ),
                                ("networks"                               ,   ("char",)    ),
                                ("orgcountry"                             ,   ("char",)    ),
                                ("orgname"                                ,   ("char",)    ),
                                ("orgstateprovince"                       ,   ("char",)    ),
                                ("pubrecord_date"                         ,   ("char",)    ),
                                ("source_url"                             ,   ("char",)    ),
                                ("url"                                    ,   ("char",)    ),
                                ("id"                                     ,   ("char",)    ),
                                ("associatedmedia"                        ,   ("char",)    ),
                                ("associatedoccurrences"                  ,   ("char",)    ),
                                ("associatedorganisms"                    ,   ("char",)    ),
                                ("associatedrefs"                         ,   ("char",)    ),
                                ("associatedsequences"                    ,   ("char",)    ),
                                ("associatedtaxa"                         ,   ("char",)    ),
                                ("bed"                                    ,   ("char",)    ),
                                ("behavior"                               ,   ("char",)    ),
                                ("catalognumber"                          ,   ("char",)    ),
                                ("continent"                              ,   ("char",)    ),
                                ("coordinateprecision"                    ,   ("char",)    ),
                                ("coordinateuncertaintyinmeters"          ,   ("char",)    ),
                                ("country"                                ,   ("char",)    ),
                                ("countrycode"                            ,   ("char",)    ),
                                ("county"                                 ,   ("char",)    ),
                                ("record_dateidentified"                  ,   ("char",)    ),
                                ("day"                                    ,   ("char",)    ),
                                ("decimallatitude"                        ,   ("char",)    ),
                                ("decimallonitude"                        ,   ("char",)    ),
                                ("disposition"                            ,   ("char",)    ),
                                ("earliestageorloweststage"               ,   ("char",)    ),
                                ("earliesteonorlowesteonothem"            ,   ("char",)    ),
                                ("earliestepochorlowestseries"            ,   ("char",)    ),
                                ("earliesteraorlowesterathem"             ,   ("char",)    ),
                                ("earliestperiodorlowestsystem"           ,   ("char",)    ),
                                ("enddayofyear"                           ,   ("char",)    ),
                                ("establishmentmeans"                     ,   ("char",)    ),
                                ("eventrecord_date"                       ,   ("char",)    ),
                                ("eventid"                                ,   ("char",)    ),
                                ("eventremarks"                           ,   ("char",)    ),
                                ("eventtime"                              ,   ("char",)    ),
                                ("fieldnotes"                             ,   ("char",)    ),
                                ("fieldnumber"                            ,   ("char",)    ),
                                ("footprintspatialfit"                    ,   ("char",)    ),
                                ("footprintsrs"                           ,   ("char",)    ),
                                ("footprintwkt"                           ,   ("char",)    ),
                                ("formation"                              ,   ("char",)    ),
                                ("geodeticdatum"                          ,   ("char",)    ),
                                ("geologicalcontextid"                    ,   ("char",)    ),
                                ("georeferencedby"                        ,   ("char",)    ),
                                ("georeferencedrecord_date"               ,   ("char",)    ),
                                ("georeferenceprotocol"                   ,   ("char",)    ),
                                ("georeferenceremarks"                    ,   ("char",)    ),
                                ("georefsources"                          ,   ("char",)    ),
                                ("georeferenceverificationstatus"         ,   ("char",)    ),
                                ("grp"                                    ,   ("char",)    ),
                                ("habitat"                                ,   ("char",)    ),
                                ("highergeography"                        ,   ("char",)    ),
                                ("highergeographyid"                      ,   ("char",)    ),
                                ("highestbiostratigraphiczone"            ,   ("char",)    ),
                                ("identificationid"                       ,   ("char",)    ),
                                ("identificationqualifier"                ,   ("char",)    ),
                                ("identificationrefs"                     ,   ("char",)    ),
                                ("identificationremarks"                  ,   ("char",)    ),
                                ("identificationverificationstatus"       ,   ("char",)    ),
                                ("identifiedby"                           ,   ("char",)    ),
                                ("individualcount"                        ,   ("char",)    ),
                                ("island"                                 ,   ("char",)    ),
                                ("islandgrp"                              ,   ("char",)    ),
                                ("latestageorhigheststage"                ,   ("char",)    ),
                                ("latesteonorhighesteonothem"             ,   ("char",)    ),
                                ("latestepochorhighestseries"             ,   ("char",)    ),
                                ("latesteraorhighesterathem"              ,   ("char",)    ),
                                ("latestperiodorhighestsystem"            ,   ("char",)    ),
                                ("lifestage"                              ,   ("char",)    ),
                                ("lithostratigraphicterms"                ,   ("char",)    ),
                                ("locality"                               ,   ("char",)    ),
                                ("locationaccordingto"                    ,   ("char",)    ),
                                ("locationid"                             ,   ("char",)    ),
                                ("locationremarks"                        ,   ("char",)    ),
                                ("lowestbiostratigraphiczone"             ,   ("char",)    ),
                                ("materialsampleid"                       ,   ("char",)    ),
                                ("maximumdepthinmeters"                   ,   ("char",)    ),
                                ("maximumdistanceabovesurfaceinmeters"    ,   ("char",)    ),
                                ("maximumelevationinmeters"               ,   ("char",)    ),
                                ("member"                                 ,   ("char",)    ),
                                ("minimumdepthinmeters"                   ,   ("char",)    ),
                                ("minimumdistanceabovesurfaceinmeters"    ,   ("char",)    ),
                                ("minimumelevationinmeters"               ,   ("char",)    ),
                                ("month"                                  ,   ("char",)    ),
                                ("municipality"                           ,   ("char",)    ),
                                ("occurrenceid"                           ,   ("char",)    ),
                                ("occurrenceremarks"                      ,   ("char",)    ),
                                ("occurrencestatus"                       ,   ("char",)    ),
                                ("organismid"                             ,   ("char",)    ),
                                ("organismname"                           ,   ("char",)    ),
                                ("organismremarks"                        ,   ("char",)    ),
                                ("organismscope"                          ,   ("char",)    ),
                                ("othercatalognumbers"                    ,   ("char",)    ),
                                ("pointradiusspatialfit"                  ,   ("char",)    ),
                                ("preparations"                           ,   ("char",)    ),
                                ("previousidentifications"                ,   ("char",)    ),
                                ("recordedby"                             ,   ("char",)    ),
                                ("recordnumber"                           ,   ("char",)    ),
                                ("reproductivecondition"                  ,   ("char",)    ),
                                ("samplingeffort"                         ,   ("char",)    ),
                                ("samplingprotocol"                       ,   ("char",)    ),
                                ("sex"                                    ,   ("char",)    ),
                                ("startdayofyear"                         ,   ("char",)    ),
                                ("stateprovince"                          ,   ("char",)    ),
                                ("typestatus"                             ,   ("char",)    ),
                                ("verbatimcoordinates"                    ,   ("char",)    ),
                                ("verbatimcoordinatesystem"               ,   ("char",)    ),
                                ("verbatimdepth"                          ,   ("char",)    ),
                                ("verbatimelevation"                      ,   ("char",)    ),
                                ("verbatimeventrecord_date"               ,   ("char",)    ),
                                ("verbatimlatitude"                       ,   ("char",)    ),
                                ("verbatimlocality"                       ,   ("char",)    ),
                                ("verbatimlonitude"                       ,   ("char",)    ),
                                ("verbatimsrs"                            ,   ("char",)    ),
                                ("waterbody"                              ,   ("char",)    ),
                                ("year"                                   ,   ("char",)    ),
                                ("type"                                   ,   ("char",)    ),
                                ("modified"                               ,   ("char",)    ),
                                ("language"                               ,   ("char",)    ),
                                ("license"                                ,   ("char",)    ),
                                ("rightsholder"                           ,   ("char",)    ),
                                ("accessrights"                           ,   ("char",)    ),
                                ("bibliographiccitation"                  ,   ("char",)    ),
                                ("dc_refs"                                ,   ("char",)    ),
                                ("institutionid"                          ,   ("char",)    ),
                                ("collectionid"                           ,   ("char",)    ),
                                ("datasetid"                              ,   ("char",)    ),
                                ("institutioncode"                        ,   ("char",)    ),
                                ("collectioncode"                         ,   ("char",)    ),
                                ("datasetname"                            ,   ("char",)    ),
                                ("ownerinstitutioncode"                   ,   ("char",)    ),
                                ("basisofrecord"                          ,   ("char",)    ),
                                ("informationwithheld"                    ,   ("char",)    ),
                                ("datageneralizations"                    ,   ("char",)    ),
                                ("dynamicproperties"                      ,   ("char",)    ),
                                ("taxonid"                                ,   ("char",)    ),
                                ("scientificnameid"                       ,   ("char",)    ),
                                ("acceptednameusageid"                    ,   ("char",)    ),
                                ("parentnameusageid"                      ,   ("char",)    ),
                                ("originalnameusageid"                    ,   ("char",)    ),
                                ("nameaccordingtoid"                      ,   ("char",)    ),
                                ("namepublishedinid"                      ,   ("char",)    ),
                                ("taxonconceptid"                         ,   ("char",)    ),
                                ("scientificname"                         ,   ("char",)    ),
                                ("acceptednameusage"                      ,   ("char",)    ),
                                ("parentnameusage"                        ,   ("char",)    ),
                                ("originalnameusage"                      ,   ("char",)    ),
                                ("nameaccordingto"                        ,   ("char",)    ),
                                ("namepublishedin"                        ,   ("char",)    ),
                                ("namepublishedinyear"                    ,   ("char",)    ),
                                ("higherclassification"                   ,   ("char",)    ),
                                ("kingdom"                                ,   ("char",)    ),
                                ("phylum"                                 ,   ("char",)    ),
                                ("class"                                  ,   ("char",)    ),
                                ("sporder"                                ,   ("char",)    ),
                                ("family"                                 ,   ("char",)    ),
                                ("genus"                                  ,   ("char",)    ),
                                ("subgenus"                               ,   ("char",)    ),
                                ("specificepithet"                        ,   ("char",)    ),
                                ("infraspecificepithet"                   ,   ("char",)    ),
                                ("taxonrank"                              ,   ("char",)    ),
                                ("verbatimtaxonrank"                      ,   ("char",)    ),
                                ("scientificnameauthorship"               ,   ("char",)    ),
                                ("vernacularname"                         ,   ("char",)    ),
                                ("nomenclaturalcode"                      ,   ("char",)    ),
                                ("taxonomicstatus"                        ,   ("char",)    ),
                                ("nomenclaturalstatus"                    ,   ("char",)    ),
                                ("taxonremarks"                           ,   ("char",)    )]
                 
            engine.table = table
            engine.create_table()
            if not os.path.isfile(engine.format_filename(filename)):                
                engine.download_files_from_archive(self.urls[tablename], [filename], filetype="gz", archivename="vertnet_latest_"+str(tablename)) 
            engine.insert_data_from_file(engine.format_filename(str(filename)))  

SCRIPT = main()