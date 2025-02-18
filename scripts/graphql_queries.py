from string import Template
def stop_data_query():
    return """ {
    stops {
        id
        gtfsId
        name
        lat
        lon
        zoneId
      }
    }
    """

def cancelled_trips_query(after = None):
    return Template("""{canceledTrips(first: 1000, after: $after) {
    pageInfo {
      hasNextPage
      endCursor
    }
    edges {
      node {
        serviceDate
        trip {
          gtfsId
          alerts (types:ROUTE) {
            alertHeaderText
            alertDescriptionText
          }
        }
        start {
          stopLocation {
            ... on Stop {
              name
            }
          }
          schedule {
            time {
              ... on ArrivalDepartureTime {
                departure
              }
            }
          }
          realTime {
            departure {
              delay
              time
            }
          }
        }
        end {
          stopLocation {
            ... on Stop {
              name
            }
          }
          schedule {
            time {
              ... on ArrivalDepartureTime {
                arrival
              }
            }
          }
          realTime {
            arrival {
              delay
              time
            }
          }
        }
      }
    }
  }
}""").substitute({'after': "null" if after is None else after})

def distruptions_query():
    return """ {
    alerts {
        alertHeaderText
        alertDescriptionText
        alertUrl
        effectiveStartDate
        effectiveEndDate
        id
        entities {
          __typename
          ... on Route {
            gtfsId
          }
        }
      }
    }
    """