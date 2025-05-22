resource "yandex_storage_bucket" "bucket" {
  bucket = var.bucket_name
  access_key = var.bucket_access_key
  secret_key = var.bucket_secret_key

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "aws:kms"
        kms_master_key_id = var.kms_key_id
      }
    }
  }
} 