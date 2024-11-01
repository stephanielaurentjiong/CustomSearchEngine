from exa_py import Exa

exa = Exa('36c051eb-3f9f-4b02-8fdd-7b7170e4025a')

query = input('Search here:')


response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()