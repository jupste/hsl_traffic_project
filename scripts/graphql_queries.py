def stop_data_query():
    return """ {
    stops {
        id,
        gtfsId
        name
        lat
        lon
        zoneId
      }
    }
    """

def cancelled_trips_query(start_cursor = None):
    return """{canceledTrips(first: 1000) {
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
  }
}"""

def distruptions_query():
    return """ {
    alerts {
        alertHeaderText
        alertDescriptionText
        alertUrl
        effectiveStartDate
        effectiveEndDate
        entities {
          __typename
          ... on Route {
            gtfsId
          }
        }
      }
    }
    """