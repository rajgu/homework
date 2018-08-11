Feature: job_search.feature
  Search for specific job and verify job offer data

  Scenario: Search and verify Quality Assurance Engineer job offer
      Given open F-Secure web page
       Then I accept cookies statement
        And I click on career button
        And I click on open jobs button
        And From available cities I select 'Poznań'
        And I click on 'Quality Engineer' offer
       When I check if 'WebDriver' is on requirements list
        And I check if 'automated testing' is on requirements list
        And I check if 'API testing' is on requirements list
        And I verify that i will be working with 'JAVIER MORENO'
        And I verify that i will be working with 'KAMIL JANOWSKI'
