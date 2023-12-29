from helpers import get_coverage

def test_coverage_by_postcode_found():
    result = get_coverage(city="Paris")
    assert result is not None
    assert result == [
    {
      "bouygues": {
        "2G": 1,
        "3G": 1,
        "4G": 1
      }
    },
    {
      "free": {
        "2G": 0,
        "3G": 1,
        "4G": 1
      }
    },
    {
      "orange": {
        "2G": 1,
        "3G": 1,
        "4G": 1
      }
    },
    {
      "sfr": {
        "2G": 1,
        "3G": 1,
        "4G": 1
      }
    }
  ]


def test_coverage_by_postcode_not_found():
    result = get_coverage("Evry-Courcouronnes")
    assert result is None
