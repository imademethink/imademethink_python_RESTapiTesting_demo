#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
from json2html import *
import sys
import os
from shutil import rmtree
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    reporting_folder_name = 'reporting_folder_json_html'
    #
    # remove if any reporting folder exists
    if os.path.exists(reporting_folder_name):
        rmtree(reporting_folder_name)
    os.makedirs(reporting_folder_name)
    #
    # allure reporting related command line arguments
    reportingRelated = ' -f allure_behave.formatter:AllureFormatter -o ' + reporting_folder_name + '  '
    #
    # feature file path
    featureFilePath = ' feature_files_folder/Simple_REST_API_Testing.feature '
    #
    # tag option (currently not using any tag)
    tagOptions = ' --tags=-tag_me '
    tagOptions = ''
    #
    # command line argument to capture console output
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    #
    # full list of command line options
    fullRunnerOptions = tagOptions + featureFilePath + reportingRelated + commonRunnerOptions
    #
    # run Behave + BDD + Python code
    runner_with_options.main(fullRunnerOptions)
    #
    # read resultant json file
    listOfJsonFiles = glob.glob(reporting_folder_name + "/*.json")
    finalJson = ''
    for cnt in range(0, len(listOfJsonFiles)):
        listOfJsonFiles[cnt] = ' {"' + "Scenario_" + str(cnt) + '"' + ' : ' + open(listOfJsonFiles[cnt], 'r').read() + '}'
        if cnt < (-1 + len(listOfJsonFiles)):
            listOfJsonFiles[cnt] = listOfJsonFiles[cnt] + ','
        finalJson = finalJson + listOfJsonFiles[cnt]
    finalJson = '[ ' + finalJson + ' ]'
    #
    # convert json to html using simple utility and publish report
    html_content = json2html.convert(json=finalJson)
    html_report_file = open(reporting_folder_name + '/' + 'index.html', 'w')
    html_report_file.write(html_content)
    html_report_file.close()
