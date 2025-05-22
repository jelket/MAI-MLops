output "bucket_name" {
  description = "The name of the bucket"
  value       = yandex_storage_bucket.bucket.bucket
}

output "bucket_domain_name" {
  description = "The domain name of the bucket"
  value       = yandex_storage_bucket.bucket.bucket_domain_name
} 